from pydantic import BaseModel, field_validator
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    price: float = 0.0
    stock_quantity: int = 0
    supplier_id: Optional[int] = None

    @field_validator("name")
    def name_nu_poate_fi_gol(cls, value):
        if not value.strip():
            raise ValueError("Numele nu poate fi gol!")
        return value

    @field_validator("sku")
    def sku_nu_poate_fi_gol(cls, value):
        if not value.strip():
            raise ValueError("SKU-ul nu poate fi gol!")
        return value

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