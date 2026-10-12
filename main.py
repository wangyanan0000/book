from fastapi import FastAPI, HTTPException
from app.router import Memo
from fastapi.middleware.cors import CORSMiddleware
from app.get_db import create_tables

app=FastAPI()

create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(Memo.router)