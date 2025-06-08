from pydantic import BaseModel
from typing import List, Optional

class ProductResponse(BaseModel):
    PRD_ID: int
    CODE: str
    NAME: str
    PRICE: int

    class Config:
        orm_mode = True

class PurchaseItem(BaseModel):
    PRD_ID: int
    CODE: str
    NAME: str
    PRICE: int

class PurchaseRequest(BaseModel):
    EMP_CD: Optional[str] = "9999999999"
    STORE_CD: Optional[str] = "30"
    POS_NO: Optional[str] = "90"
    items: List[PurchaseItem]

class PurchaseResponse(BaseModel):
    success: bool
    total_amount: int
