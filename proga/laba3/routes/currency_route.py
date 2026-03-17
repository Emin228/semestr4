
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from set import DbCurrency, get_db
from ht import fetch_curr
import xml.etree.ElementTree as ET

router = APIRouter(tags=["Currencies"])

@router.get('/currencies')
async def GetCurrencies(db: Session = Depends(get_db)):
    currencies = db.execute(
        select(DbCurrency)
    ).scalars().all()
    
    if not  currencies:
        return {"message": "Db is empty"}
    return currencies

    

@router.post('/currencies/update')
async def dd(db: Session = Depends(get_db)):
    
    data = await fetch_curr()
    root = ET.fromstring(data)
   

    for valute in root.findall('Valute'):
        cur_id = valute.get('ID')
        
        exists = db.query(DbCurrency).filter(DbCurrency.id == cur_id).first()
        
        code = valute.findtext('CharCode')
        name = valute.findtext('Name')
        if not exists:
            cur = DbCurrency(
                id=cur_id,
                code=code,
                name=name
            )   
            db.add(cur)
    db.commit()
    all_currencies = db.query(DbCurrency).all()
    return {
        "currencies": [
            {"id": c.id, "code": c.code, "name": c.name} 
            for c in all_currencies]
    }
