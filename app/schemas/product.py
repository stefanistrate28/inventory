from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    price: float = 0.0
    stock_quantity: int = 0
    supplier_id: Optional[int] = None

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    supplier_id: Optional[int] = None

class ProductResponse(ProductCreate):
    id: int
    warehouse_id: int

    model_config = {"from_attributes": True}