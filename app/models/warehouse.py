from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location = Column(String(200))
    description = Column(String(500))

    # un warehouse are mai multe produse
    products = relationship("Product", back_populates="warehouse", cascade="all, delete-orphan")