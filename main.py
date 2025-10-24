from generate.generate_image import generate_image
from generate.generate_video import generate_video
from s3_utils import upload_to_s3, write_urls_to_html

# Generate an image and upload
image_file = generate_image()
image_s3_path = f"images/{image_file.split('/')[-1]}"
image_url = upload_to_s3(image_file, image_s3_path)

# Generate a video and upload
video_file = generate_video()
video_s3_path = f"videos/{video_file.split('/')[-1]}"
video_url = upload_to_s3(video_file, video_s3_path)

# Write URLs into index.html automatically
write_urls_to_html(image_url, video_url)
