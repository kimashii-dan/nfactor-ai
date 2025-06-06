from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel


load_dotenv()  

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

agent = create_react_agent(llm=llm)

messages = [
    (
        "system",
        "You are the assistant who verifies if the given fact is the truth. Output True or False.",
    ),
]

class VerifyerRequest(BaseModel):
    text: str


app = FastAPI()
@app.post("/verify")
def analyze(request: VerifyerRequest):
    messages.append(("human", request))
    ai_msg = llm.invoke(messages)
    return ai_msg.content
