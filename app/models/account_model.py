from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.config.db import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    id_client = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="accounts")
    movements = relationship("Movement", back_populates="account")
