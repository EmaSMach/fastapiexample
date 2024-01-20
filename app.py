from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models import User


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/users/")
def users_list(request: Request):
    users = [
        User(first_name="John", last_name="last_name", age=35, address="USA", phone="111", email="", password=""),
        User(first_name="Mary", last_name="last_name", age=25, address="USA", phone="222", email="", password=""),
        User(first_name="Bob", last_name="last_name", age=30, address="USA", phone="333", email="", password=""),
    ]
    return {
        "count": len(users),
        "results": users
    }


@app.post("/users/")
def create_user(user: User):
    return user
