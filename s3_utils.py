import boto3

# Initialize S3 client
s3 = boto3.client('s3', region_name='ap-southeast-1')
bucket_name = "my-generative-ai-bucket"

def upload_to_s3(local_file_path, s3_object_name):
    """
    Upload a file to S3 and return a pre-signed URL.
    """
    s3.upload_file(local_file_path, bucket_name, s3_object_name)
    print(f"{local_file_path} uploaded to {bucket_name}/{s3_object_name}")

    # Generate pre-signed URL
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': s3_object_name},
        ExpiresIn=3600
    )
    return url

def write_urls_to_html(image_url, video_url, html_path="index.html"):
    """
    Insert the pre-signed URLs into index.html dynamically.
    """
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Generative AI Outputs</title>
</head>
<body>
    <h1>Uploaded Generative AI Files</h1>

    <h2>Image</h2>
    <img src="{image_url}" alt="Generated Image" width="400">

    <h2>Video</h2>
    <video width="400" controls>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>"""

    with open(html_path, "w") as f:
        f.write(html_content)
    print(f"index.html updated with new URLs")
