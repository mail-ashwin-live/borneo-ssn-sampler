import boto3

def init():
    s3client = boto3.client('s3')
    return s3client

def get_file_count(client):
    # get the bucket
    response = client.list_buckets()
    count_obj = 0
    for bucket in response['Buckets']:
        s3bucket = client.Bucket(bucket)
        for i in s3bucket.objects.all():
            count_obj = count_obj + 1
    print(count_obj)
    return(count_obj)