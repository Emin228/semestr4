from fastapi import FastAPI

from routes.user_route import router as user_route
from routes.currency_route import router as currencies_route
from routes.subscription_route import router as sub_route

app = FastAPI()
app.include_router(user_route)
app.include_router(currencies_route)
app.include_router(sub_route)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", reload=True)


