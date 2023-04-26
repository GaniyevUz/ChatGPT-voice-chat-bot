from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'sqlite:///example.db'
engine = create_engine(db_url)


def get_session(autocommit=False):
    return sessionmaker(bind=engine, autocommit=autocommit).begin()
