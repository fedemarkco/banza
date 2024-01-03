from sqlalchemy import Column, ForeignKey, Integer, Enum, DateTime, Float
from sqlalchemy.orm import relationship
from app.models import MovementEnum
from datetime import datetime
from app.config.db import Base


class Movement(Base):
    __tablename__ = "movements"

    id = Column(Integer, primary_key=True, index=True)
    id_account = Column(Integer, ForeignKey("accounts.id"))
    type = Column(Enum(MovementEnum))
    amount = Column(Float, default=0)
    date = Column(DateTime, default=datetime.now())

    account = relationship("Account", back_populates="movements")
