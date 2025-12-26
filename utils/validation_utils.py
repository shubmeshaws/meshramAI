```python
import re
import logging

from utils.error_handling import handle_error

logger = logging.getLogger(__name__)

def validate_aws_region(region):
    """
    Validate if the given AWS region is valid.
    """
    try:
        with open('regions.conf', 'r') as f:
            valid_regions = [line.strip() for line in f.readlines()]
            if region not in valid_regions:
                handle_error(f"Invalid AWS region: {region}")
    except FileNotFoundError:
        handle_error("regions.conf file not found")

def validate_s3_bucket_name(bucket_name):
    """
    Validate if the given S3 bucket name is valid.
    """
    if not re.match('^[a-z0-9.-]{3,63}$', bucket_name):
        handle_error(f"Invalid S3 bucket name: {bucket_name}")

def validate_ec2_instance_id(instance_id):
    """
    Validate if the given EC2 instance ID is valid.
    """
    if not re.match('^(i-[0-9a-f]{8,18})$', instance_id):
        handle_error(f"Invalid EC2 instance ID: {instance_id}")

def validate_vpc_id(vpc_id):
    """
    Validate if the given VPC ID is valid.
    """
    if not re.match('^(vpc-[0-9a-f]{8,17})$', vpc_id):
        handle_error(f"Invalid VPC ID: {vpc_id}")
```
