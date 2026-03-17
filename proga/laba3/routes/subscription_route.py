from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from set import  get_db, sub_table
from modules.sub_module import SubModule

router = APIRouter(tags=["Subs"])

@router.post('/subscriptions')
async def SubUser(user_id: int, currency_id: str, db: Session = Depends(get_db)):
    sub_exist = db.execute(
        select(sub_table).where(
            sub_table.c.user_id == user_id,
            sub_table.c.currency_id == currency_id
        )
    ).scalars().all()
    

    if sub_exist:
        raise HTTPException(status_code=409, detail="Sub already exists")

    db.execute(
        sub_table.insert().values(user_id=user_id, currency_id=currency_id)
    )
    db.commit()

    return {"message": "Subscribed"}

@router.get('/subscriptions/{user_id}', response_model=list[SubModule])
async def GetUserSub(user_id: int, db: Session = Depends(get_db)):
    get_subs = db.query(sub_table).where(
        sub_table.c.user_id == user_id
    ).all()
    if not get_subs:
        raise HTTPException (status_code=404, detail="Sub doesnt exist ")
    
    return get_subs
   

@router.delete('/subscriptions_delete')
async def DeleteSubUser(user_id: int, currency_id: str, db: Session = Depends(get_db)):
    sub = db.execute(
        sub_table.delete().where(
            sub_table.c.user_id == user_id,
            sub_table.c.currency_id == currency_id)
    )
    
    if sub.rowcount == 0:
        db.rollback()
        raise HTTPException(status_code=404, detail="Sub not found")
    db.commit()
    
    return {"message": "Sub deleted successfully"}
