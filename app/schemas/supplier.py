from pydantic import BaseModel, field_validator
from typing import Optional

class SupplierCreate(BaseModel):
    name: str
    contact_email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

    @field_validator("name")
    def name_nu_poate_fi_gol(cls, value):
        if not value.strip():
            raise ValueError("Numele nu poate fi gol!")
        return value

class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    contact_email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class SupplierResponse(SupplierCreate):
    id: int

    model_config = {"from_attributes": True}