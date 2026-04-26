from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.inventory import MovementCreate, MovementResponse
from app.schemas.product import ProductResponse
from app.services import inventory_service

router = APIRouter()

@router.get("/", response_model=list[ProductResponse])
def get_inventory(warehouse_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_inventory(db, warehouse_id)

@router.get("/{product_id}/movements", response_model=list[MovementResponse])
def get_movements(warehouse_id: int, product_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_movements(db, warehouse_id, product_id)

@router.post("/{product_id}/stock-in", response_model=MovementResponse)
def stock_in(warehouse_id: int, product_id: int, data: MovementCreate, db: Session = Depends(get_db)):
    return inventory_service.stock_in(db, warehouse_id, product_id, data)

@router.post("/{product_id}/stock-out", response_model=MovementResponse)
def stock_out(warehouse_id: int, product_id: int, data: MovementCreate, db: Session = Depends(get_db)):
    return inventory_service.stock_out(db, warehouse_id, product_id, data)

@router.post("/{product_id}/transfer", response_model=MovementResponse)
def transfer(warehouse_id: int, product_id: int, data: MovementCreate, db: Session = Depends(get_db)):
    return inventory_service.transfer(db, warehouse_id, product_id, data)