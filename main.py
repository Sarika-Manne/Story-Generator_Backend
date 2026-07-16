from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

from chat import generate_story

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/generate-story")
async def generate(
    image: UploadFile = File(...),
    genre: str = Form(...),
    length: str = Form(...)
):
    img = Image.open(io.BytesIO(await image.read()))

    story = generate_story(img, genre, length)

    return {"story": story}