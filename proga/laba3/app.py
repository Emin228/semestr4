from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from routes.user_route import router as user_route
from routes.currency_route import router as currencies_route
from ht import fetch_curr

from set import DbCurrency, get_db, sub_table
import xml.etree.ElementTree as ET
from pydantic import BaseModel


app = FastAPI()
app.include_router(user_route)
app.include_router(currencies_route)


@app.post('/subscriptions')
async def SubUser(user_id: int, currency_id: str, db: Session = Depends(get_db)):
    sub_exist = db.execute(
        select(sub_table).where(
            sub_table.c.user_id == user_id,
            sub_table.c.currency_id == currency_id
        )
    ).scalar_one_or_none()
    

    if sub_exist:
        raise HTTPException(status_code=400, detail="Sub already exists")

    db.execute(
        sub_table.insert().values(user_id=user_id, currency_id=currency_id)
    )
    db.commit()

    return {"message": "Subscribed"}

@app.get('/subscriptions/{user_id}')
async def GetUserSub(user_id: int, db: Session = Depends(get_db)):
    get_subs = db.execute(
        select(sub_table).where(
            sub_table.c.user_id == user_id
        )
    ).scalars().all()
    
    if not get_subs:    
        raise HTTPException (status_code=400, detail="Sub doesnt exist ")
    return get_subs

@app.delete('/subscriptions_delete')
async def DeleteSubUser(user_id: int, currency_id: str, db: Session = Depends(get_db)):
    sub = db.get(sub_table, user_id)
    if not sub:
        raise HTTPException(status_code=404, detail="Sub not found")
    return 
    db.delete(sub)
    db.commit()
    return {"message": "Sub deleted successfully"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", reload=True)


