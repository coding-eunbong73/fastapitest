from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#sqlite3
#SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

#postgresql
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:New1234!!@localhost/TodoApplicationDatabase"


engine = create_engine(
    # sqlite3
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}

    # postgresql
    SQLALCHEMY_DATABASE_URL

)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
