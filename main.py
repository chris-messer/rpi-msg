from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel



app = FastAPI()
class MessageModel(BaseModel):
    message: str

@app.get("/")
async def root(request: Request):
    pckg = dict(request.query_params)
    msg = pckg.get('Body','')
    print(msg)
    return {"status": 200}


if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)