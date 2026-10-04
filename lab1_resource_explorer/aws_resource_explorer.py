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


show_identity()
show_region()