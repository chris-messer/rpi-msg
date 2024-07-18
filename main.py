import os
print(os.getcwd())

from fastapi import FastAPI, Form, Response, Request, HTTPException
import uvicorn
from twilio.twiml.messaging_response import MessagingResponse
from twilio.request_validator import RequestValidator
from dotenv import load_dotenv
from app.external_services.service_ngrok import get_ngrok_url
from app.external_services.service_twilio import set_webhook_address
from app.utils.create_message import text_to_image
from app.display.print_to_eink import print_img
from app.utils.utils import get_project_root
from pydantic import BaseModel
from typing import Union, Optional
import requests


class Msg(BaseModel):
    message: str
class Mms(BaseModel):
    From: str


import os
load_dotenv()

server_url = get_ngrok_url()
set_webhook_address(server_url+'/hook')

app = FastAPI()

@app.post("/hook")
async def chat(
    request: Request,
    MediaUrl0: Optional[str] = Form(None),
    From: Optional[str] = Form(None),
    Body: Optional[str] = Form(None)
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
    # msg = response.message(f"Hi {From}, you said: {Body}")
    img = text_to_image(Body)
    print_img(img)
    return Response(content=str(response), media_type="application/xml")


@app.post("/dev")
async def root(msg: Msg):
    msg = msg.message
    img = text_to_image(msg)
    print_img(img)
    return {"status": 200}

uvicorn.run(app, host="0.0.0.0", port=8000)