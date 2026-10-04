import boto3


def show_identity():
    sts = boto3.client("sts")
    identity = sts.get_caller_identity()
    print("WHO AM I?")
    print(f"Account ID : {identity['Account']}")
    print(f"User ID    : {identity['UserId']}")
    print(f"ARN        : {identity['Arn']}")


show_identity()