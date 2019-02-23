from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, NCHAR
from sqlalchemy.orm import relationship


class DenysOrders(Base):
    __tablename__ = 'DenysOrders'

    id = Column(String(40), primary_key=True, unique=True, nullable=False)
    name = Column(Integer)
    description = Column(String)
    moment = Column(DateTime, nullable=False)
    sum = (Column, Integer)
    counterparty_id = Column(String(40), ForeignKey('DenysClients.id'), nullable=False)

    counterparty = relationship("DenysClients")


class DenysClients(Base):
    __tablename__ = 'DenysClients'

    id = Column(String(40), primary_key=True, unique=True, nullable=False)
    name = Column(NCHAR(length=100), nullable=False,)
