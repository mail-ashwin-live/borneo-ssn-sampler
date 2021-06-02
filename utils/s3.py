import boto3
import pandas as pd 
import random 

def flip(p):
    return 1 if random.random() < p else 0

def get_file_count():
    client = boto3.client('s3') 
    resource = boto3.resource('s3')
    response = client.list_buckets()
    count_obj = 0
    fileList = []
    for bucket in response['Buckets']:
        s3bucket = resource.Bucket(bucket['Name'])
        for key in s3bucket.objects.all():
            if key.size:
                fileList.append(bucket['Name'] + '/' +key.key)
                count_obj = count_obj + 1
    return(count_obj, fileList)

def get_subset_files(fileList, num_files):
    files = random.choices(fileList, k=num_files)
    return(files)