import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config.db_config import DATABASE_URL, ISOLATION_LEVEL



def create_database_session():
    engine = sqlalchemy.create_engine(DATABASE_URL,isolation_level=ISOLATION_LEVEL, echo=False, future=True)
    Session = sessionmaker(bind=engine)
    return Session()