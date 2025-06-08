from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from crud.product import get_product_by_code
from models.schema import ProductResponse

router = APIRouter()

@router.get("/product", response_model=ProductResponse)
def read_product(code: str = Query(...), db: Session = Depends(get_db)):
    product = get_product_by_code(db, code)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
