from fileinput import filename
import boto3
import pandas as pd


s3_client = boto3.client("s3")
filename="temp.json"
for user in [12,13,14]:
    for day in [22,23,24]:
        for obj in range(100):
            object_name = f"year=2022/month=05/day={day}/user={user}/{obj}.json"
            df = pd.DataFrame({'duration': range(6), 'user': user, 'day': day})
            _ = df.to_json(filename)
            
            _ = s3_client.upload_file(filename, 'lambda-test-abcd', object_name)