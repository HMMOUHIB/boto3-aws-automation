import boto3


def show_identity():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    print("WHO AM I?")
    print(f"Account ID : {identity['Account']}")
    print(f"User ID    : {identity['UserId']}")
    print(f"ARN        : {identity['Arn']}")


def show_region():
    session = boto3.session.Session()
    print("CURRENT REGION")
    print(f"Region  : {session.region_name}")
    print(f"Profile : {session.profile_name}")


def list_buckets_with_client():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    print("S3 BUCKETS (via client)")
    for bucket in response["Buckets"]:
        created = bucket["CreationDate"].strftime("%Y-%m-%d %H:%M")
        print(f"  {bucket['Name']:<45} created {created}")
    print(f"Total: {len(response['Buckets'])} bucket(s)")


show_identity()
show_region()
list_buckets_with_client()