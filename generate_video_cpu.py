import time
from diffusers import StableVideoDiffusionPipeline
import torch
from PIL import Image
from moviepy import ImageSequenceClip

def main():
    print("🚀 generate_video_cpu.py starting...")

    # Load pipeline
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "yihong-chen/StableVideoDiffusion-CPU",
        torch_dtype=torch.float32,
    ).to("cpu")

    # Input image (replace with your filename)
    input_path = "input.png"
    init_image = Image.open(input_path).convert("RGB").resize((512, 512))

    # Parameters for high quality output
    num_frames = 24
    steps = 25
    fps = 6
    prompt = "A high quality cinematic animation from this image"

    print(f"📥 Generating {num_frames} frames at {fps} FPS...")

    frames = pipe(
        prompt=prompt,
        init_image=init_image,
        num_inference_steps=steps,
        num_frames=num_frames
    ).frames

    # Save video with MoviePy
    timestamp = int(time.time())
    output_file = f"output_{timestamp}.mp4"

    clip = ImageSequenceClip([f for f in frames], fps=fps)
    clip.write_videofile(output_file, codec="libx264", fps=fps)

    print(f"✅ High quality video saved to {output_file}")

if __name__ == "__main__":
    main()
