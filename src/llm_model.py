from llama_index.llms.groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
Groq_api_key=os.getenv("GROQ_API_KEY")
def Groq_model():
    return Groq(model="qwen/qwen3-32b",api_key=Groq_api_key)