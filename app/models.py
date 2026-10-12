from sqlalchemy import Column,INTEGER,String
from app.get_db import Base

class Memo(Base):
    __tablename__="memo"
    id=Column(INTEGER,primary_key=True,autoincrement=True)
    title=Column(String(50),nullable=False)
    content=Column(String(100),nullable=False)