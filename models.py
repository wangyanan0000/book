from MySQLdb.constants.FLAG import PRI_KEY
from sqlalchemy import Column,INTEGER,String
from get_db import Base
class Memo(Base):
    _tablename_="memo"
    id=Column(INTEGER,primary_key=True,autioncrement=True)
    title=Column(String(50),nullable=False)
    content=Column(String(100),nullable=False)

