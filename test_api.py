import requests

def test_generate_image(prompt):
    url = "http://127.0.0.1:5000/generate-image"
    payload = {"prompt": prompt}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        if "image_url" in data:
            print("Image generated successfully!")
            print("Image URL:", data["image_url"])
        else:
            print("Error in response:", data.get("error", "No image_url found"))
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    prompt_text = "a fantasy castle on a hill under a sunset sky"
    test_generate_image(prompt_text)
