from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


users = {
    1: {
        'username': 'A',
        'age': 20,
        'country': None,
        'email': 'qwert@gmail.com'
    },
    2: {
        'username': 'B',
        'age': 27,
        'country': 'Russia',
        'email': 'asdfg@gmail.com'
    }
}

class User(BaseModel):
    username: str
    age: int
    country: Optional[str] = None
    email: str

class UpdateUser(BaseModel):
    username: Optional[str] = None
    age: Optional[int] = None
    country: Optional[str] = None
    email: Optional[str] = None

@app.get("/users/")
async def gerUsers():
    return users 

@app.post("/create-user/{user_id}")
async def create_user(user_id: int, new_user: User):
    if user_id in users:
        return {'Error': 'User already exists'}
    users[user_id] = new_user
    return users[user_id]

@app.put("/update-users/{user_id}")
async def update_user(user_id: int, upd_user: UpdateUser):
    if user_id not in users:
        return {'Error': 'User ID does not exists'}
    

    current_user = users[user_id]
    if upd_user.username is not None:
        current_user['username'] = upd_user.username
    if upd_user.age is not None:
        current_user['age'] = upd_user.age
    if upd_user.country is not None:
        current_user['country'] = upd_user.country
    if upd_user.email is not None:
        current_user['email'] = upd_user.email        
    return users[user_id]


@app.get("/users/{user_id}")
async def getUsers(user_id: int):
    return users[user_id]

@app.delete('/delete-user')
async def DelteUser(user_id: int = Query(..., description='Id greater than zero')):
    if user_id not in users:
        return {'Error':'User ID does not exists'}
    del users[user_id]
    return {'Done': 'User was succesfuly deleted'}


@app.post('/subscriptions')
async def SubUser(user_id, currency_id):
    pass

@app.delete('/subscriptions')
async def DeleteSubUser(user_id, currency_id):
    pass

@app.get('/currencies')
async def GetCurrencies():
    pass

@app.post('/currencies/update')
async def dd():
    pass

