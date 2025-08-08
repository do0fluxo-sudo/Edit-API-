from fastapi import FastAPI
from pydantic import BaseModel
import requests
from io import BytesIO
from PIL import Image
import torch
from fastapi.responses import StreamingResponse
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

app = FastAPI()

# Load model
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
    "timbrooks/instruct-pix2pix", torch_dtype=torch.float32
)
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to("cpu")

class EditRequest(BaseModel):
    image_url: str
    instruction: str

@app.post("/edit-image")
async def edit_image(data: EditRequest):
    response = requests.get(data.image_url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image = image.resize((512, 512))

    output_img = pipe(image=image, prompt=data.instruction, num_inference_steps=20).images[0]

    output_bytes = BytesIO()
    output_img.save(output_bytes, format="JPEG")
    output_bytes.seek(0)

    return StreamingResponse(output_bytes, media_type="image/jpeg")
