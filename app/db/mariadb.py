from core import config
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

db_url = URL(
    drivername=config.DB['DIALECT'],
    username=config.DB['USER'],
    password=config.DB['PASSWORD'],
    host=config.DB['HOST'],
    port=config.DB['PORT'],
    database=config.DB['NAME'],
)


engine = create_engine(db_url)

Session = sessionmaker(engine, expire_on_commit=False, class_=Session)

Model = declarative_base()


def init_db():
    import models  # noqa

    Model.metadata.create_all(engine)
