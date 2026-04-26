from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.supplier import SupplierCreate, SupplierUpdate, SupplierResponse
from app.services import supplier_service

router = APIRouter()

@router.post("/", response_model=SupplierResponse)
def create_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_service.create_supplier(db, data)

@router.get("/", response_model=list[SupplierResponse])
def get_suppliers(db: Session = Depends(get_db)):
    return supplier_service.get_all_suppliers(db)

@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return supplier_service.get_supplier_by_id(db, supplier_id)

@router.patch("/{supplier_id}", response_model=SupplierResponse)
def patch_supplier(supplier_id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    return supplier_service.patch_supplier(db, supplier_id, data)

@router.put("/{supplier_id}", response_model=SupplierResponse)
def put_supplier(supplier_id: int, data: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_service.put_supplier(db, supplier_id, data)