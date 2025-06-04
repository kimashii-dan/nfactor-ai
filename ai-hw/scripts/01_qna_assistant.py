import openai
from dotenv import load_dotenv
import os

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

vector_store = client.vector_stores.create(name="My Vector Store")

file = client.files.create(
    file=open("data/attention-ai.pdf", "rb"),
    purpose="assistants"
)
client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=file.id
)


response = client.responses.create(
    input="How training data works?",
    model="gpt-4o",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id],
    }]
)

print(response.output[1].content[0].text) 