from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_database_url = '{engine}://{user}:{password}@{host}:{port}/{database}'.format(
                engine='postgresql+psycopg2',
                user="postgres",
                password="nopassword",
                host="localhost",
                port="5432",
                database="internet"
            )

engine = create_engine(sqlalchemy_database_url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
