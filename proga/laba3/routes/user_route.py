from fastapi import FastAPI, Depends, HTTPException, APIRouter
from requests import Session
from sqlalchemy import select
from sqlalchemy.orm import Session
from modules.user_module import User, UpdateUser
from set import  DbUser, get_db

router = APIRouter(tags=["User"])

@router.post("/create-user/")
async def create_user(new_user: User, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(DbUser).where(DbUser.username == new_user.username)
    ).scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    db_user = DbUser(
        username = new_user.username,
        email=new_user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/")
async def gerUsers(db: Session= Depends(get_db)):
    users = db.execute(
        select(DbUser)
    ).scalars().all()
    if not users:
        return {"message": "Users count = 0"}
    return users

@router.get("/users/{user_id}")
async def getUsers(user_id: int, db: Session = Depends(get_db)):
    current_user = db.execute(
        select(DbUser).where(DbUser.id == user_id)
    ).scalar_one_or_none()

    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return current_user


@router.put("/update-users/{user_id}")
async def update_user(user_id: int, upd_user: UpdateUser, db: Session = Depends(get_db)):
    user = db.get(DbUser, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if upd_user.username:
        user.username = upd_user.username
    if upd_user.email:
        user.email = upd_user.email

    db.commit()
    db.refresh(user)

    return user





@router.delete('/delete-user/{user_id}')
async def DelteUser(user_id: int, db: Session = Depends(get_db)):
    user = db.get(DbUser, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
