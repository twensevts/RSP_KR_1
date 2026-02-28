from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from models import User, Feedback

app = FastAPI()


class CalculateInput(BaseModel):
    num1: float
    num2: float


feedbacks = []


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content


@app.post("/calculate")
async def calculate(data: CalculateInput):
    result = data.num1 + data.num2
    return {"result": result}


@app.get("/users")
async def get_users():
    return {
        "name": "Ваше Имя и Фамилия",
        "id": 1
    }


@app.post("/user")
async def check_user(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }


@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

