import os
from dotenv import load_dotenv
from google import genai
# Load variables from .env
load_dotenv()
# Read API key securely
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)

from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    course: str
    sentiment: Literal["Positive", "Negative", "Neutral"]
    rating: int = Field(ge=1, le=5)
