from .base import *  # noqa
from .base import env  # noqa


# for s3
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", default=None)
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")

# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# STATIC
# ------------------------
STATICFILES_STORAGE = "apps.utils.storages.StaticRootS3Boto3Storage"
#
# MEDIA
# ------------------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "apps.utils.storages.MediaRootS3Boto3Storage"
MEDIA_URL = f"https://{aws_s3_domain}/media/"
