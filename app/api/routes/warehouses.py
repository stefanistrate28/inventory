from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.warehouse import WarehouseCreate, WarehouseUpdate, WarehouseResponse
from app.services import warehouse_service

router = APIRouter()

@router.post("/", response_model=WarehouseResponse)
def create_warehouse(data: WarehouseCreate, db: Session = Depends(get_db)):
    return warehouse_service.create_warehouse(db, data)

@router.get("/", response_model=list[WarehouseResponse])
def get_warehouses(db: Session = Depends(get_db)):
    return warehouse_service.get_all_warehouses(db)

@router.get("/{warehouse_id}", response_model=WarehouseResponse)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    return warehouse_service.get_warehouse_by_id(db, warehouse_id)

@router.patch("/{warehouse_id}", response_model=WarehouseResponse)
def patch_warehouse(warehouse_id: int, data: WarehouseUpdate, db: Session = Depends(get_db)):
    return warehouse_service.patch_warehouse(db, warehouse_id, data)

@router.put("/{warehouse_id}", response_model=WarehouseResponse)
def put_warehouse(warehouse_id: int, data: WarehouseCreate, db: Session = Depends(get_db)):
    return warehouse_service.put_warehouse(db, warehouse_id, data)