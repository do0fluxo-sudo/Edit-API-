# NIROB API
# 🖼️ AI Image Edit API (InstructPix2Pix)

This is a FastAPI-based image editing API that uses natural language instructions to modify images using AI (Stable Diffusion InstructPix2Pix model).

## ✨ Features

- Edit images using plain text instructions
- Based on Stable Diffusion InstructPix2Pix
- Deployable on Render.com (free tier)
- Easy integration with bots (e.g., GOATBOT)

---

## 🚀 Example Usage

**POST** `/edit-image`

### 🔸 Request Body (JSON):
```json
{
  "image_url": "https://i.ibb.co/XYZ.jpg",
  "instruction": "remove logo and change background"
}
