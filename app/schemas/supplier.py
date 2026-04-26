from pydantic import BaseModel
from typing import Optional

class SupplierCreate(BaseModel):
    name: str
    contact_email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    contact_email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class SupplierResponse(SupplierCreate):
    id: int

    model_config = {"from_attributes": True}