from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine(
    "mysql+mysqlconnector://root@localhost/college_db",
    echo=True
)
