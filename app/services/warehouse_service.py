from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate

def create_warehouse(db: Session, data: WarehouseCreate):
    # cream un warehouse nou
    warehouse = Warehouse(**data.model_dump())
    db.add(warehouse)
    db.commit()
    db.refresh(warehouse)
    return warehouse

def get_all_warehouses(db: Session):
    return db.query(Warehouse).all()

def get_warehouse_by_id(db: Session, warehouse_id: int):
    warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse-ul nu a fost gasit")
    return warehouse

def patch_warehouse(db: Session, warehouse_id: int, data: WarehouseUpdate):
    warehouse = get_warehouse_by_id(db, warehouse_id)
    # actualizam doar campurile trimise
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(warehouse, key, value)
    db.commit()
    db.refresh(warehouse)
    return warehouse

def put_warehouse(db: Session, warehouse_id: int, data: WarehouseCreate):
    warehouse = get_warehouse_by_id(db, warehouse_id)
    # actualizam toate campurile
    for key, value in data.model_dump().items():
        setattr(warehouse, key, value)
    db.commit()
    db.refresh(warehouse)
    return warehouse