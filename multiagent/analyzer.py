import os
from typing import Literal, Union
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic import BaseModel
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class MyOutput(BaseModel):
    classification: Literal["fact", "opinion", "hypothesis", "question"]
    
    
class AnalyzeRequest(BaseModel):
    text: str

model = OpenAIModel('gpt-4o', provider=OpenAIProvider(api_key=api_key))
analyzer_agent = Agent(
    model, deps_type=str, 
    output_type=MyOutput, 
    system_prompt="You are a classification agent. Your task is to analyze a given statement and determine its type. Classify the input into exactly one of the following categories: - fact: A verifiable and objective truth. - opinion: A personal belief, feeling, or preference that cannot be universally verified. - hypothesis: A testable assumption or proposed explanation that is not yet proven. - question: An inquiry or request for information.")


app = FastAPI()
@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = analyzer_agent.run_sync(request.text)
    return {"response": result.output}

