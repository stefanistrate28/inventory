from pydantic import BaseModel
from typing import Optional

class WarehouseCreate(BaseModel):
    name: str
    location: Optional[str] = None
    description: Optional[str] = None

class WarehouseUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

class WarehouseResponse(WarehouseCreate):
    id: int

    model_config = {"from_attributes": True}