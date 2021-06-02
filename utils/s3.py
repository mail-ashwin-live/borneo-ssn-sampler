import boto3

def get_file_count():
    # get the bucket
    client = boto3.client('s3') 
    s3 = boto3.resource('s3')
    response = client.list_buckets()
    count_obj = 0
    for bucket in response['Buckets']:
        print(bucket['Name'])
        s3bucket = s3.Bucket(bucket['Name'])
        for key in s3bucket.objects.all():
            count_obj = count_obj + 1
    return(count_obj)

