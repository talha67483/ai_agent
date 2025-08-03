from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
import os




load_dotenv(override=True)

my_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")
ai_model = os.getenv("AI_MODEL")





client = AsyncOpenAI(api_key=my_api_key,base_url=base_url)

Model = OpenAIChatCompletionsModel(openai_client=client,model=ai_model)
