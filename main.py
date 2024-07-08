from fastapi import FastAPI, Form, Response, Request, HTTPException
import uvicorn
from pydantic import BaseModel
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv
from utils.establish_ngrok import get_ngrok_url
from utils.set_twilio_hook import set_webhook_address

import os
load_dotenv()

server_url = get_ngrok_url()
set_webhook_address(server_url+'/hook')

app = FastAPI()

@app.post("/hook")
async def chat(
    request: Request, From: str = Form(...), Body: str = Form(...)
):
    validator = RequestValidator(os.environ["TWILIO_AUTH_TOKEN"])
    form_ = await request.form()
    if not validator.validate(
        str(request.url),
        form_,
        request.headers.get("X-Twilio-Signature", "")
    ):
        raise HTTPException(status_code=400, detail="Error in Twilio Signature")

    response = MessagingResponse()
    msg = response.message(f"Hi {From}, you said: {Body}")
    return Response(content=str(response), media_type="application/xml")


if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)