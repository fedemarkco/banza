from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.config.db import Base
from app.models import MovementEnum


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)
    id_account = Column(Integer, ForeignKey("accounts.id"))
    type = Column(Enum(MovementEnum))
    amount = Column(Float, default=0)
    date = Column(DateTime, default=datetime.now())

    account = relationship("Account", back_populates="movements")
