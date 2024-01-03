from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class CategoryClient(Base):
    __tablename__ = "categories_clients"

    id = Column(Integer, primary_key=True, index=True)

    id_category = Column(Integer, ForeignKey("categories.id"))
    id_client = Column(Integer, ForeignKey("clients.id"))

    category = relationship("Category", back_populates="category_client")
    client = relationship("Client", back_populates="category_client")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    category_client = relationship("CategoryClient", back_populates="category")
