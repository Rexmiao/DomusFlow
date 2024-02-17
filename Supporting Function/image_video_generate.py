import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
video_model_id = "7qkldg93"
image_model_id = "8w67oe0q"
baseten_api_key = "fXFV4Kc3.pGZG3bywECzJFnbgreASZVXeiOHoGVdV"
BASE64_PREAMBLE = "data:image/png;base64,"
file_path = "description.txt"

# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

with open(file_path, 'r') as file:
    file_contents = file.read()

data = {
  "prompt": file_contents
}
# Call model endpoint
res = requests.post(
    f"https://model-{image_model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
output = res.get("data")

# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.png")
os.system("open output_image.png")

def base64_to_mp4(base64_string, output_file_path):
    binary_data = base64.b64decode(base64_string)
    with open(output_file_path, "wb") as output_file:
        output_file.write(binary_data)

def mp4_to_base64(file_path: str):
    with open(file_path, "rb") as mp4_file:
        binary_data = mp4_file.read()
        base64_data = base64.b64encode(binary_data)
        base64_string = base64_data.decode("utf-8")
    return base64_string

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

data = {
  "image": image_to_base64("./output_image.png"),
  "num_frames": 50,
  "fps": 25,
  "decoding_t": 10,
  "duration": 2
}

# Call model endpoint
res = requests.post(
    f"https://model-{video_model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key cCa3xKMc.wFezUNugVQGX9vDfsPUqpbxcEc05f9LJ"},
    json=data
)

# Get the output of the model
res = res.json()
base64_output = res.get("output")

# Convert the base64 output to an mp4 video
base64_to_mp4(base64_output, "stable-video-diffusion-output.mp4")