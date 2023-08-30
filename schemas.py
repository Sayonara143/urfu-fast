from pydantic import BaseModel
import datetime


class PriceBase(BaseModel):
    name: str
    price: int
    


class PriceCreate(PriceBase):
    pass



class Price(PriceBase):
    id: int
    datetime: datetime.datetime

    class Config:
        orm_mode = True
