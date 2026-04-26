from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services import product_service

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product(warehouse_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, warehouse_id, data)

@router.get("/", response_model=list[ProductResponse])
def get_products(warehouse_id: int, db: Session = Depends(get_db)):
    return product_service.get_all_products(db, warehouse_id)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(warehouse_id: int, product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product_by_id(db, warehouse_id, product_id)

@router.patch("/{product_id}", response_model=ProductResponse)
def patch_product(warehouse_id: int, product_id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return product_service.patch_product(db, warehouse_id, product_id, data)

@router.put("/{product_id}", response_model=ProductResponse)
def put_product(warehouse_id: int, product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    return product_service.put_product(db, warehouse_id, product_id, data)

@router.delete("/{product_id}")
def delete_product(warehouse_id: int, product_id: int, db: Session = Depends(get_db)):
    product_service.delete_product(db, warehouse_id, product_id)
    return {"message": "Produsul a fost sters"}