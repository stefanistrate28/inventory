from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    sku = Column(String(50), unique=True, index=True)
    description = Column(String(500))
    price = Column(Float, default=0.0)
    stock_quantity = Column(Integer, default=0)

    warehouse_id = Column(Integer, ForeignKey("warehouses.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)

    warehouse = relationship("Warehouse", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    inventory_movements = relationship("InventoryMovement", back_populates="product")