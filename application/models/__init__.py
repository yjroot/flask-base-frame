import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, Unicode, UnicodeText, DateTime
from sqlalchemy.sql import functions

from config import Config

database_config = Config('Database')
ENGINE_URL = database_config['url']

engine = sqlalchemy.create_engine(ENGINE_URL)

Session = sqlalchemy.orm.sessionmaker(bind=engine, autocommit=True)
Base = sqlalchemy.ext.declarative.declarative_base(engine)


class Foo(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), nullable=False,
                        default=functions.now())

    name = Column(Unicode(255), nullable=False)
    description = Column(UnicodeText, nullable=False)

    def __repr__(self):
        return "<Note('%d', '%s','%s')>" %\
            (self.id, self.name, self.description)
