import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Assign the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if it loaded properly
if api_key:
    print("✅ API key loaded successfully!")
    print("Partial key (safe):", api_key[:8] + "..." + api_key[-5:])
else:
    print("❌ API key not loaded. Check your .env file.")