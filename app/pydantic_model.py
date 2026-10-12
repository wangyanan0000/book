from pydantic import BaseModel
from typing import Optional

class MemoCreate(BaseModel):
    title:str
    content:str

class MemoUpdate(BaseModel):
    title:str|None=None
    content:str|None=None

class MemoRead(BaseModel):
    id:int
    title:str
    content:str
    model_config={"from_attributes":True}

