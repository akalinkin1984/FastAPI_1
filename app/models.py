import datetime

import sqlalchemy as sq
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import DSN

engine = create_async_engine(DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):

    @property
    def id_dict(self):
        return {"id": self.id}


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(128), nullable=False)
    description = sq.Column(sq.String(256), nullable=False)
    price = sq.Column(sq.Float, nullable=False)
    author = sq.Column(sq.String(128), nullable=False)
    create_date = sq.Column(sq.DateTime, default=datetime.date.today())

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'author': self.author,
            'create_date': int(self.create_date.timestamp()),
        }


ORM_OBJECT = Advertisement
ORM_CLS = type[Advertisement]
