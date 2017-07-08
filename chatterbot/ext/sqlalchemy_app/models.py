from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import (
    declared_attr, declarative_base
)


Base = declarative_base()


class BaseMixin(Base):
    """
    A mixin class for SqlAlchemy models.
    """
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(
        Integer,
        primary_key=True
    )
