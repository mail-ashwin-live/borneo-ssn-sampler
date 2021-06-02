import boto3
from botocore.exceptions import ClientError

def init():
    client = boto3.client('comprehend')
    return client

def detect_ssn(client, text):
    try:
        response = client.detect_pii_entities(Text=text, LanguageCode='en')
        entities = response['Entities']
    except ClientError:
        print("Couldn't detect PII entities.")
        raise
    else:
        return entities