import os

from dotenv import load_dotenv
load_dotenv()


token = os.environ.get("OPENAI_API_KEY")

print(token)

