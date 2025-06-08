from sqlalchemy.orm import Session
from models.models import Transaction, TransactionDetail
from models.schema import PurchaseRequest

def register_transaction(db: Session, purchase: PurchaseRequest):
    transaction = Transaction(
        EMP_CD=purchase.EMP_CD,
        STORE_CD=purchase.STORE_CD,
        POS_NO=purchase.POS_NO
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    total = 0
    for idx, item in enumerate(purchase.items):
        detail = TransactionDetail(
            TRD_ID=transaction.TRD_ID,
            DTL_ID=idx + 1,
            PRD_ID=item.PRD_ID,
            PRD_CODE=item.CODE,
            PRD_NAME=item.NAME,
            PRD_PRICE=item.PRICE
        )
        total += item.PRICE
        db.add(detail)

    transaction.TOTAL_AMT = total
    db.commit()
    return {"success": True, "total_amount": total}
