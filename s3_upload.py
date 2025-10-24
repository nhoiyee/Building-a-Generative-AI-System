import boto3

# Initialize S3 client
s3 = boto3.client('s3', region_name='ap-southeast-1')
bucket_name = "my-generative-ai-bucket"

def upload_to_s3(local_file_path, s3_object_name):
    """
    Upload a file to S3 bucket and return a pre-signed URL.
    
    :param local_file_path: Path to the local file
    :param s3_object_name: Path in the S3 bucket
    :return: pre-signed URL for temporary access
    """
    # Upload file
    s3.upload_file(local_file_path, bucket_name, s3_object_name)
    print(f"{local_file_path} uploaded to {bucket_name}/{s3_object_name}")

    # Generate pre-signed URL (valid for 1 hour)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': s3_object_name},
        ExpiresIn=3600
    )
    return url
