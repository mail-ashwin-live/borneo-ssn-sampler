import argparse
import utils.comprehend as ml
import utils.s3 as s3
import utils.stats_module as sm 
import numpy as np 

def get_ssn_output(local, fileList):
    client = ml.init()
    ssnList = []
    ssnScores = []
    for file in fileList:
        ssn, score = 0,0
        text = s3.get_file_text(local, file)
        if text != "":
            ssn, score = ml.detect_ssn(client, text)
        ssnList.append(ssn)
        ssnScores.append(score)
    return (ssnList, ssnScores)

def main():
    
    parser = argparse.ArgumentParser(description="program to detect SSN presence in files")
    parser.add_argument('--cl', '-confidence-level', type=float, default=0.95, help="required confidence from the sampling algorithm (default value of 0.5)")
    parser.add_argument('--me', '-margin-error', type=float, default=0.05, help="required margin of error from the sampling algorithm (default value of 0.05)")
    args = parser.parse_args() 
    local = False
    # count the total sample size 
    num_files, fileList = s3.get_file_count(local, './data/output/')

    # set the confidence level, margin of error and population size 
    confidence_level = args.cl 
    margin_error = args.me 
    pop_size = num_files 

    # get the sample size needed 
    sample_size = round(sm.sampleSize(pop_size, margin_error, confidence_level))

    print('For the number of files', pop_size, ' at a confidence level ', confidence_level, ' with margin of error ', margin_error, \
        ' sample size needed is ', sample_size)

    # run Pass 1 
    print("running first pass of detection.... ")
    sampled_files_a = s3.get_subset_files(fileList, sample_size)

    ssnList_a, ssnScores_a = get_ssn_output(local, sampled_files_a)

    print("running second pass of detection.... ")
    sampled_files_b = s3.get_subset_files(fileList, sample_size)

    ssnList_b, ssnScores_b = get_ssn_output(local, sampled_files_b)
    #print("detected SSN: ", ssnList)

    mean_per = (np.mean(ssnList_a) + np.mean(ssnList_b) )/2 
    tot_files = round((np.sum(ssnList_a) + np.sum(ssnList_b) )/2 )
    measure_a = 0 
    measure_b = 0 

    for i in range(len(ssnList_a)):
        if ssnList_a[i] == 1:
            measure_a += ssnScores_a[i]
        if ssnList_b[i] == 1:
            measure_b += ssnScores_b[i]
    
    measure_a = measure_a / np.sum(ssnList_a)
    measure_b = measure_b / np.sum(ssnList_b)
    measure = (measure_a + measure_b)/2 

    hypothesis = sm.ttest(ssnList_a, ssnList_b, confidence_level)
    if hypothesis:
        print('In ', sample_size, ' number of files, detected ', tot_files, ' files with SSN. With a confidence of ', (100*confidence_level), 'percent and '\
            ' margin of error being +/-', (100*margin_error),' percent. The SSN detection algorithm worked with a confidence of ', (measure*100), ' percent')
    else: 
        print('Unable to give conclusive evidence of SSNs detected. Try increasing the confidence interval or reducing margin of error')


if __name__ == "__main__":
    main()
