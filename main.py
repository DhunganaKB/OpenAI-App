from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain import PromptTemplate
import os
from generate import generate
import uvicorn

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["MODEL_NAME"] = MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)

app = FastAPI()

class Body(BaseModel):
    text: str

@app.get("/")
def welcome():
    return {"message": "Welcome to the LLMApp!"}


@app.post("/response")
def generate_response(body: Body):
    question = body.text
    result = generate(question, llm, PromptTemplate)
    return {"response": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
