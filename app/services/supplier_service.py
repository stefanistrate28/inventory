from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate, SupplierUpdate

def create_supplier(db: Session, data: SupplierCreate):
    supplier = Supplier(**data.model_dump())
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

def get_all_suppliers(db: Session):
    return db.query(Supplier).all()

def get_supplier_by_id(db: Session, supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier-ul nu a fost gasit")
    return supplier

def patch_supplier(db: Session, supplier_id: int, data: SupplierUpdate):
    supplier = get_supplier_by_id(db, supplier_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(supplier, key, value)
    db.commit()
    db.refresh(supplier)
    return supplier

def put_supplier(db: Session, supplier_id: int, data: SupplierCreate):
    supplier = get_supplier_by_id(db, supplier_id)
    for key, value in data.model_dump().items():
        setattr(supplier, key, value)
    db.commit()
    db.refresh(supplier)
    return supplier