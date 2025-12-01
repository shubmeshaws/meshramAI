```python
import os
import boto3
from botocore.exceptions import NoCredentialsError

def get_aws_session(profile_name=None, region_name=None):
    """
    Returns an AWS session object.

    Args:
        profile_name (str, optional): The AWS profile name. Defaults to None.
        region_name (str, optional): The AWS region name. Defaults to None.

    Returns:
        boto3.Session: The AWS session object.
    """
    try:
        if profile_name:
            session = boto3.Session(profile_name=profile_name, region_name=region_name)
        else:
            session = boto3.Session(region_name=region_name)
        return session
    except NoCredentialsError:
        print("AWS credentials not found. Please configure your AWS credentials.")
        return None

def get_aws_service_client(service_name, session=None):
    """
    Returns an AWS service client object.

    Args:
        service_name (str): The AWS service name (e.g., 'ec2', 's3', 'vpc').
        session (boto3.Session, optional): The AWS session object. Defaults to None.

    Returns:
        boto3.client: The AWS service client object.
    """
    if not session:
        session = get_aws_session()
    if session:
        return session.client(service_name)
    else:
        return None

def get_aws_config(region_name=None):
    """
    Returns the AWS configuration.

    Args:
        region_name (str, optional): The AWS region name. Defaults to None.

    Returns:
        dict: The AWS configuration.
    """
    config = {
        'region_name': region_name if region_name else os.environ.get('AWS_REGION'),
        'access_key_id': os.environ.get('AWS_ACCESS_KEY_ID'),
        'secret_access_key': os.environ.get('AWS_SECRET_ACCESS_KEY')
    }
    return config
```
