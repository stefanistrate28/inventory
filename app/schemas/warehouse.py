from pydantic import BaseModel, field_validator
from typing import Optional

class WarehouseCreate(BaseModel):
    name: str
    location: Optional[str] = None
    description: Optional[str] = None

    @field_validator("name")
    def name_nu_poate_fi_gol(cls, value):
        if not value.strip():
            raise ValueError("Numele nu poate fi gol!")
        return value

class WarehouseUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

class WarehouseResponse(WarehouseCreate):
    id: int

    model_config = {"from_attributes": True}