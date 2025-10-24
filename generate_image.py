import argparse
import time
from diffusers import StableDiffusionPipeline
import torch

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output", default="generated_image.png", help="Output image filename")
    parser.add_argument("--fast", action="store_true", help="Enable fast mode (fewer steps, lower res)")
    args = parser.parse_args()

    print("🚀 generate_image.py starting...")
    print(f"📝 Prompt: {args.prompt}\n💾 Output: {args.output}\n⚡ Fast mode: {args.fast}")

    # Load pipeline
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32,
    ).to("cpu")

    # Inference steps and resolution
    steps = 10 if args.fast else 25
    width, height = (256, 256) if args.fast else (512, 512)

    print(f"📥 Generating image at {width}x{height} with {steps} steps...")

    image = pipe(
        args.prompt,
        num_inference_steps=steps,
        width=width,
        height=height
    ).images[0]

    # Save with timestamp to avoid overwrite
    timestamp = int(time.time())
    output_file = args.output.replace(".png", f"_{timestamp}.png")
    image.save(output_file)

    print(f"✅ Image saved to {output_file}")

if __name__ == "__main__":
    main()
