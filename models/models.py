from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP, ForeignKey
from .database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    PRD_ID = Column(Integer, primary_key=True, index=True)
    CODE = Column(CHAR(13), unique=True, nullable=False)
    NAME = Column(String(50), nullable=False)
    PRICE = Column(Integer, nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"
    TRD_ID = Column(Integer, primary_key=True, index=True)
    DATETIME = Column(TIMESTAMP, default=datetime.utcnow)
    EMP_CD = Column(CHAR(10), default="9999999999")
    STORE_CD = Column(CHAR(5), default="30")
    POS_NO = Column(CHAR(3), default="90")
    TOTAL_AMT = Column(Integer, default=0)

class TransactionDetail(Base):
    __tablename__ = "transaction_details"
    TRD_ID = Column(Integer, ForeignKey("transactions.TRD_ID"), primary_key=True)
    DTL_ID = Column(Integer, primary_key=True)
    PRD_ID = Column(Integer)
    PRD_CODE = Column(CHAR(13))
    PRD_NAME = Column(String(50))
    PRD_PRICE = Column(Integer)
