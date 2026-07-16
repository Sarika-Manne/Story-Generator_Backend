import os
from google import genai
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def generate_story(image, genre, length):
    if image is None:
        return "Please upload an image."
    prompt = f"""
    You are a creative storyteller.
    Analyze the uploaded image and write a {genre} story.
    Story Length: {length}
    Requirements:
    - Give the story a title.
    - Introduce characters.
    - Describe the scene.
    - Build an interesting plot.
    - End with a meaningful conclusion.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[image, prompt]
    )
    return response.text