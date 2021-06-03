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
        if not entities:
            return (0,0)
        for r in entities:
            if r.get('Type') == 'SSN' and r.get("Score") > 0.85:
                return (1,r.get("Score"))
            else:
                return (0,r.get("Score"))