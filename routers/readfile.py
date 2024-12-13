import os
from fastapi import APIRouter
from dotenv import load_dotenv
from controllers import readfile

load_dotenv()

router = APIRouter(
    prefix="/read",
    tags=["Read File"],
    responses={404: {"description": "Not found"}},
)

token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

@router.post("/all_xlsx")
async def all_xlsx():
   result = readfile.all_xlsx()
   return result

@router.post("/key_xlsx")
async def key_xlsx(key: str):
   result = readfile.key_xlsx(key)
   return result
