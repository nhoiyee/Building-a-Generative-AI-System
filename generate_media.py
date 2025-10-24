import argparse
import torch
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
from PIL import Image
import time
import imageio

def generate_image(prompt, fast=False):
    print("🖼️ Starting text-to-image...")

    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )
    pipe.to("cpu")
    pipe.enable_attention_slicing()  # saves memory

    steps = 10 if fast else 15
    width, height = (256, 256) if fast else (512, 512)

    image = pipe(prompt, num_inference_steps=steps, width=width, height=height).images[0]

    filename = f"generated_image_{int(time.time())}.png"
    image.save(filename)
    print(f"✅ Image saved to {filename}")
    return filename


def generate_video(image_path, prompt, fast=False):
    print("🎬 Starting image-to-video...")

    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid",
        torch_dtype=torch.float32
    )
    pipe.to("cpu")
    pipe.enable_attention_slicing()        # memory-efficient
    pipe.enable_model_cpu_offload()       # offload weights to CPU/disk

    image = Image.open(image_path).convert("RGB")
    image = image.resize((256, 256))  # small resolution

    num_frames = 4 if fast else 6
    steps = 8 if fast else 12
    fps = 6

    frames = pipe(
        prompt=prompt,
        init_image=image,
        num_inference_steps=steps,
        num_frames=num_frames
    ).frames

    filename = f"generated_video_{int(time.time())}.mp4"
    imageio.mimsave(filename, frames, fps=fps)
    print(f"✅ Video saved to {filename}")
    return filename


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt for generation")
    parser.add_argument("--fast", action="store_true", help="Enable faster but lower-quality mode")
    args = parser.parse_args()

    print("🚀 generate_media.py starting...")
    print(f"📝 Prompt: {args.prompt}")
    print(f"⚡ Fast mode: {args.fast}")

    # Step 1: Text-to-Image
    img_path = generate_image(args.prompt, args.fast)

    # Step 2: Image-to-Video
    vid_path = generate_video(img_path, args.prompt, args.fast)

    print(f"\n🎉 Done! Outputs:\n🖼️ {img_path}\n🎬 {vid_path}")


if __name__ == "__main__":
    main()
