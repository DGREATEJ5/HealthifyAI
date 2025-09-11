from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("GEMINI_API_KEY loaded:", GEMINI_API_KEY)  # Should show your key, not None

# Set explicitly (needed for langchain_google_genai)
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY  # <-- Use GOOGLE_API_KEY not GEMINI_API_KEY

# Initialize Gemini model
chatModel = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Test Gemini
try:
    response = chatModel.invoke("Hello, are you working?")
    print("Full response object:", response)  # Debug
    print("Gemini says:", response.content)  # ✅ This is the text you want
except Exception as e:
    print("Gemini error:", e)
