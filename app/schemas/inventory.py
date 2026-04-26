from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.inventory import MovementType

class MovementCreate(BaseModel):
    movement_type: MovementType
    quantity: int
    notes: Optional[str] = None

class MovementResponse(BaseModel):
    id: int
    product_id: int
    movement_type: MovementType
    quantity: int
    notes: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}