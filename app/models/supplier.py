from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contact_email = Column(String(150))
    phone = Column(String(30))
    address = Column(String(300))

    # un supplier poate furniza mai multe produse
    products = relationship("Product", back_populates="supplier")