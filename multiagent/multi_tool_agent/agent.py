from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from google.adk.agents import Agent

load_dotenv()

capital_agent = Agent(
    model="gemini-2.0-flash",
    name="verifyer_agent",
    description="You are verifyer agent who can check if the fact is actually truth",
    instruction="Verify if the given fact is truth"
)



# class VerifyRequest(BaseModel):
#     text: str

# app = FastAPI()

# @app.post("/analyze")
# def analyze(request: VerifyRequest):

