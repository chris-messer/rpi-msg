from dotenv import load_dotenv
import ngrok
import os

load_dotenv()

def get_ngrok_url():
    listener = ngrok.forward("localhost:22", authtoken=os.getenv('NGROK_AUTHTOKEN'),
    proto="tcp")
    listener = ngrok.forward(8000, authtoken=os.getenv('NGROK_AUTHTOKEN'))
    # Output ngrok url to console
    return listener.url()

if __name__ == "__main__":
   get_ngrok_url()