from pydantic import BaseModel

class SubModule(BaseModel):
    user_id: int
    currency_id: str

    class Config:
        orm_mode = True
