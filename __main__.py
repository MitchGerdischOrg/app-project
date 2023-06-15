# App project Template
import pulumi
from pulumi_aws import s3

my_bucket = s3.BucketV2('my-bucket')

my_bucket_access_block = s3.BucketPublicAccessBlock('my-bucket-access-block',
                                                    bucket=my_bucket.id, 
                                                    # block_public_acls=True
                                                    )