from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models.schema import PurchaseRequest, PurchaseResponse
from crud.transaction import register_transaction

router = APIRouter()

@router.post("/purchase", response_model=PurchaseResponse)
def create_purchase(data: PurchaseRequest, db: Session = Depends(get_db)):
    try:
        return register_transaction(db, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
