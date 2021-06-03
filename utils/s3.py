import boto3
import pandas as pd 
import random 
import os 

def flip(p):
    return 1 if random.random() < p else 0

def get_file_count(local_flag, path='~/'):
    if not local_flag:
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
    else:
        fileList = []
        num_files = 0
        for base, dirs, files in os.walk(path):
            #print('Searching in : ',base)
            for file in files:
                if not file.startswith('.'):
                    fileList.append(base + '/' + file)
                    num_files += 1
        return(num_files, fileList)

def get_subset_files(fileList, num_files):
    files = random.choices(fileList, k=num_files)
    return(files)

def get_file_text(local, path):
    if not local:
        bucket, key = path.split('/')
        client = boto3.client('s3')
        s3_object = client.get_object(Bucket=bucket, Key=key)
        body = s3_object['Body']
        return body.read().decode('utf-8')
    else: 
        file = open(path, 'r')
        text = file.read()
        file.close()
        return(text)