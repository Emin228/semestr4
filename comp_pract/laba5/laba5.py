from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

quotes = [
    "Ученье — свет.",
    "Без труда не вытащишь и рыбку из пруда."
]

class Quote(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Добро пожаловать в коллекцию цитат!"}

@app.get("/quotes")
def get_quotes():
    return {"quotes": quotes}

@app.post("/quotes")
def add_quote(quote: Quote):
    quotes.append(quote.text)
    return {
        "message": "Цитата добавлена",
        "quote": quote.text
    }