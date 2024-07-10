import boto3
import os 

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
print('end')

arr = os.listdir('.')
print(arr)