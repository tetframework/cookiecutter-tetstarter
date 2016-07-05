from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from . import Base, DBSession

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)
