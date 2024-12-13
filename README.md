# Line OA API Webhook



# Installation
Clone the repository

Use Git:

```
git clone -b ECOP https://gitlab.com/tencode/line-oa-api-webhook.git
cd line-oa-api-webhook
```

Use Python:
Create env folder with python3

```
python3 -m venv env
source env/bin/activate
```

Use Pip:

```
pip install -r requirements.txt --upgrade pip
```

## Test
Run Server Test with hypercorn [-b "IP:PORT"]

```
hypercorn main:app --reload -b "0.0.0.0:8000"
```

# Deploy
- sudo nano /etc/systemd/system/webhookapi.service

```
[Unit]
Description=Webhook API modules

[Service]
Type=simple
User={user}
Group={group}
ExecStart=/Users/{user}/line-oa-api-webhook/env/bin/python3 -m hypercorn /Users/{user}/line-oa-api-webhook/main:app --reload --bind "0.0.0.0:8000" --access-log /Users/{user}/line-oa-api-webhook/access-log -w 4 -k asyncio
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

```

- sudo systemctl daemon-reload
- sudo systemctl enable --now webhookapi

