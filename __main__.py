"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Main bucket
platform_bucket = s3.BucketV2('platform-bucket')
platform_bucket_public_access_block = s3.BucketPublicAccessBlock('platform-bucket-access', s3.BucketPublicAccessBlockArgs(
    bucket=platform_bucket.id,
    block_public_acls=True,
    block_public_policy=True,
    ignore_public_acls=True,
    restrict_public_buckets=True,
))

# Export the name of the bucket
pulumi.export('platform_bucket_name', platform_bucket.id)
