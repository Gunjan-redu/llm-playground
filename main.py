import anthropic
from fastapi import  FastAPI, HTTPException
from sdk import talk
from pydantic import BaseModel

app = FastAPI()


class AskIn(BaseModel):
    question: str

@app.post("/ask" )
def ask(body: AskIn):
    try:
        message = talk(body.question)
        return {"answer":message}
    except anthropic.APITimeoutError:
        raise HTTPException(status_code =504, detail ="LLM service timed out")
    except anthropic.APIError:
        raise HTTPException(status_code =502, detail ="LLM service error")

