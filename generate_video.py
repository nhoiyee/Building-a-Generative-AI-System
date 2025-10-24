# generate_video.py
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import os

def create_video_from_images(image_folder, output_file="output.mp4", fps=24):
    """
    Create a video from images in a folder.
    
    Args:
        image_folder (str): Path to folder containing image frames
        output_file (str): Path to save the output video
        fps (int): Frames per second
    """
    # Collect image files (assuming .png or .jpg)
    images = sorted(
        [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".png", ".jpg"))]
    )

    if not images:
        raise ValueError("No images found in the folder!")

    # Create video clip
    clip = ImageSequenceClip(images, fps=fps)

    # Write the video file
    clip.write_videofile(output_file, codec="libx264")

if __name__ == "__main__":
    # Example usage
    create_video_from_images("input_frames", output_file="test.mp4", fps=24)
