# import json
import os
# from pydantic import BaseModel
# from typing import Optional
import requests
from fastapi import APIRouter, Request, Body
from dotenv import load_dotenv
from controllers import webhook
# from ai import translate

load_dotenv()

router = APIRouter(
    prefix="/webhooks",
    tags=["Chatbot"],
    responses={404: {"description": "Not found"}},
)

token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

@router.post("/check/format/")
async def check_format(text: Request):
   result = await text.json()
   return result

@router.post("/line/broadcast/")
async def line_broadcast(text: str):
   result = webhook.line_broadcast(text)
   return result

@router.get("/line/push/{to}/{topic}")
async def line_push(topic: str, text: Request,to: str):
   data = await text.json()
   result = webhook.line_push(topic, data, to)
   return result

@router.get("/line/multicast/{to}/{topic}")
async def line_multicast(topic: str, text: Request,to: str):
   data = await text.json()
   result = webhook.line_multicast(topic, data, to)
   return result

@router.get("/line/narrowcast/{to}/{topic}")
async def line_narrowcast(topic: str, text: Request,to: str):
   data = await text.json()
   result = webhook.line_narrowcast(topic, data, to)
   return result
