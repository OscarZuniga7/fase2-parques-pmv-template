import os
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from functools import lru_cache

@lru_cache(maxsize=1)
def engine():
    url=URL.create('mysql+pymysql', username=os.getenv('DB_USER','alumno'),password=os.getenv('DB_PASSWORD','alumno_demo_cambiar'),host=os.getenv('DB_HOST','localhost'),port=int(os.getenv('DB_PORT','3307')),database=os.getenv('DB_NAME','parques'))
    return create_engine(url,pool_pre_ping=True,pool_recycle=1800)

def fetch(sql,params=None):
    with engine().connect() as c:return [dict(r) for r in c.execute(text(sql),params or {}).mappings()]

def execute(sql,params=None):
    with engine().begin() as c:return c.execute(text(sql),params or {})
