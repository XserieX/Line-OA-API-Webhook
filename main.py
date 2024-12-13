# include_in_schema=False
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from routers import webhook, readfile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = [
    "*"
    # "http://localhost",
    # "https://localhost:8443",
    # "https://localhost:8443",
    # "https://localhost:8443",
    # "https://192.168.0.10",
    # "https://ti-serv1.bcg-ecop.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

# app.mount("/css", StaticFiles(directory="css"), name="css")


# templates = Jinja2Templates(directory="pages")

# @app.get("/{id}", response_class=HTMLResponse, include_in_schema=False)
# async def read_item(request: Request, id: int):
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"id": id}
#     )


def config_router():
    app.include_router(readfile.router)
    app.include_router(webhook.router)
    # app.include_router(generate.router)

config_router()