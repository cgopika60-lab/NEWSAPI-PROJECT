import boto3
import json
from datetime import datetime


s3 = boto3.client(
    "s3",
    region_name="ap-south-1"
)

bucket_name = "news-api2"


def upload_to_s3(final_data):

    try:

        file_name = (
            f"news_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(final_data)
        )

        print(f"Uploaded to S3: {file_name}")

    except Exception as e:

        print("S3 ERROR:", e)