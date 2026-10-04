import os
import sys

import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
REGION = boto3.session.Session().region_name or "us-east-1"

MENU = """
=========================================
 S3 MANAGER
=========================================
 1. Create Bucket      5. Download File
 2. List Buckets       6. Delete File
 3. Upload File        7. Generate Presigned URL
 4. List Files         8. Delete Bucket
 9. Backup Local Folder   0. Exit
=========================================
"""

def create_bucket():
    name = input("New bucket name: ").strip()
    try:
        if REGION == "us-east-1":
            s3.create_bucket(Bucket=name)
        else:
            s3.create_bucket(
                Bucket=name,
                CreateBucketConfiguration={"LocationConstraint": REGION},
            )
        print(f"Created bucket '{name}'")
    except ClientError as e:
        code = e.response["Error"]["Code"]
        if code == "BucketAlreadyExists":
            print("That name is taken by another AWS account.")
        elif code == "BucketAlreadyOwnedByYou":
            print("You already own that bucket.")
        else:
            print(f"[AWS ERROR] {code}")


def list_buckets():
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        print(f"  {bucket['Name']}")
    print(f"Total: {len(response['Buckets'])} bucket(s)")



def upload_file():
    print("upload_file")


def list_objects():
    print("list_objects")


def download_file():
    print("download_file")


def delete_file():
    print("delete_file")


def generate_presigned_url():
    print("generate_presigned_url")


def delete_bucket():
    print("delete_bucket")


def backup_folder():
    print("backup_folder")


ACTIONS = {
    "1": create_bucket,
    "2": list_buckets,
    "3": upload_file,
    "4": list_objects,
    "5": download_file,
    "6": delete_file,
    "7": generate_presigned_url,
    "8": delete_bucket,
    "9": backup_folder,
}


def main():
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            sys.exit(0)
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")


main()