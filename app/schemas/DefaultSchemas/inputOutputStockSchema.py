import datetime

from pydantic import BaseModel


class InputOutputStockBase(BaseModel):
    type: str
    qtd: float
    date: datetime.datetime
    product_id: int
    user_id: int


class InputOutputStockCreate(InputOutputStockBase):
    id: int


class InputOutputStock(InputOutputStockBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
