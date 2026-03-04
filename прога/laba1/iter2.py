from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def func():
    return {"message":"хэлоу ворлд"}

