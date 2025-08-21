from .base import *

DEBUG = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

# AWS Region
AWS_SES_REGION_NAME = "us-east-2"
AWS_SES_REGION_ENDPOINT = "email.us-east-2.amazonaws.com"
AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')


# Email server configuration
EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'email-smtp.us-east-2.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True