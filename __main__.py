# App project Template

import pulumi
from pulumi_aws import s3

app_bucket = s3.BucketV2("app-bucket")

app_bucket_access_block = s3.BucketPublicAccessBlock("app-bucket-access-block", s3.BucketPublicAccessBlockArgs(
    bucket=app_bucket.id,
    block_public_acls=True,
    block_public_policy=True,
))

