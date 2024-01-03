from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.db import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    accounts = relationship("Account", back_populates="client")
    category_client = relationship("CategoryClient", back_populates="client")
