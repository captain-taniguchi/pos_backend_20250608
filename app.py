from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import product, purchase
from models.database import Base, engine, init_db

Base.metadata.create_all(bind=engine)

# テーブルの初期化
init_db()

app = FastAPI()
app.include_router(product.router)
app.include_router(purchase.router)

# ✅ CORS設定（3000と3001の両方を許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
