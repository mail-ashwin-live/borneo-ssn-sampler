# borneo-ssn-sampler

Code to Sample files from S3 bucket and detect if the files have SSN numbers in them 

It uses an off-the-shelf algorithm, AWS Comprehend, to detect PII identities.

The sampling works the following way:
1. for a given population size, confidence level and margin of error, we use the z-score to select a sampling size 
2. given the sample size, we run two passes of detection for SSNs with the same sample size. 
3. the output is run through a t-test to see if we are meeting the criteria for acceptance or rejection of the samples (p-value = 1 - confidence_level) 

Based on the Hypothesis test, we are able to conclude that X% of the documents have SSNs in them. Varying the confidence level and margin of error will lead to change in sampling size, thus impacting the Accuracy Vs Speed.
