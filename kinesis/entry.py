import requests
import boto3
import json
import time

from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

kinesis_client = boto3.client(
    'kinesis',
     region_name='eu-central-1',
     aws_access_key_id=getenv('ACCESS_KEY'),
     aws_secret_access_key=getenv('SECRET_KEY'),)

partition_key = "ajeiojaeiojhahewio jiowejf ioweujhfoewiafh oroiejfio wenuarei"

payload = {'dataType': 'json',}

a=0
while a< 5000:
    r = requests.get('https://randomuser.me/api/', params=payload)
    _ = kinesis_client.put_record(
        StreamName=getenv('KINESIS_STREAM_NAME'),
        Data=json.dumps(r.json()),
        PartitionKey=partition_key)
    time.sleep(0.2)
    a +=1

print('Done!')
# print(r.url)
# # print(r.text)
# print(r.json())