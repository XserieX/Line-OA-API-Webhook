import os
import requests
import json
from dotenv import load_dotenv
from controllers import readfile
from datetime import datetime

load_dotenv()

token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')

def line_broadcast(text: str):
    url = "https://api.line.me/v2/bot/message/broadcast"
    
    payload = json.dumps({
    "messages": [
        {
        "type": "text",
        "text": text
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    requests.request("POST", url, headers=headers, data=payload)
    result = { 'message': 'Successful!' }
    return result

def line_push(topic: str, data: str, to: str):
    year = data['@timestamp'].split("-")[0]
    month = data['@timestamp'].split("-")[1]
    day = data['@timestamp'].split("-")[2].split("T")[0]

    timeset = data['@timestamp'].split("T")[1]
    
    hr = timeset.split(":")[0]
    mn = timeset.split(":")[1]
    sc = timeset.split(":")[2][:-1]
    # check = year,month,day,hr,mn,sc
    specific_date = datetime(int(year), int(month), int(day), int(hr)+7, int(mn), int(str(sc)[:-1]))
    dates = str(specific_date).split(" ")[0]
    times = str(specific_date).split(" ")[1]

    url = "https://api.line.me/v2/bot/message/push/"

    payload = json.dumps({
    "to": f"{to}", # Ce6fc525964622cd2bbb60c83cc80d0b0 - group
    "messages": [
        {
        "type": "text",
        "text": f"""{topic.split('-')[0]}

{readfile.key_xlsx(topic)[0]} เข้าสู่ระบบโดย IP: {data['src_ip_addr']}

ช่วงเวลาที่เกิดขึ้น {dates} {times} น.

โปรดใช้ Dashboard [Investigate - MJC] ในการหาข้อมูลเพิ่มเติม

Query ที่ใช้ในการหาข้อมูล

{readfile.key_xlsx(topic)[1]}"""
        }
        # ,{
        # "type": "text",
        # "text": "Hello, world2"
        # }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    requests.request("POST", url, headers=headers, data=payload)
    result = { 'message': 'Successful!' }
    return result

def line_multicast(topic: str, data: str, to: str):
    url = "https://api.line.me/v2/bot/message/multicast"

    payload = json.dumps({
    "to": [
    f"{to}",
    "U760b1c276d81be960b64dd2ad0d4be07"
    ],
    "messages": [
        {
        "type": "text",
        "text": f"""{topic}
{data['text']}"""
        }
        # ,{
        # "type": "text",
        # "text": "Hello, world2"
        # }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    requests.request("POST", url, headers=headers, data=payload)
    result = { 'message': 'Successful!' }
    return result

def line_narrowcast(topic: str, data: str, to: str):
    url = "https://api.line.me/v2/bot/message/narrowcast"

    payload = json.dumps({
    "to": [
    f"{to}",
    "Ce6fc525964622cd2bbb60c83cc80d0b0"
    ],
    "messages": [
        {
        "type": "text",
        "text": f"""ระบบแจ้งเตือนอัตโนมัติ

Dear Security Analyst,

{topic} เข้าสู่ระบบโดย IP: {data['src_ip_addr']}

ช่วงเวลาที่เกิดขึ้น {data['@timestamp']}

โปรดใช้ Dashboard [Investigate - MJC] ในการหาข้อมูลเพิ่มเติม

Query ที่ใช้ในการหาข้อมูล

{data['fingerprint']}"""
        }
        # ,{
        # "type": "text",
        # "text": "Hello, world2"
        # }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    requests.request("POST", url, headers=headers, data=payload)
    result = { 'message': 'Successful!' }
    return result