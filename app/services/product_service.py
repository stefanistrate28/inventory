from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def create_product(db: Session, warehouse_id: int, data: ProductCreate):
    # verificam daca sku-ul exista deja
    existing = db.query(Product).filter(Product.sku == data.sku).first()
    if existing:
        raise HTTPException(status_code=400, detail="SKU-ul exista deja")
    
    product = Product(**data.model_dump(), warehouse_id=warehouse_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_all_products(db: Session, warehouse_id: int):
    return db.query(Product).filter(Product.warehouse_id == warehouse_id).all()

def get_product_by_id(db: Session, warehouse_id: int, product_id: int):
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.warehouse_id == warehouse_id
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produsul nu a fost gasit")
    return product

def patch_product(db: Session, warehouse_id: int, product_id: int, data: ProductUpdate):
    product = get_product_by_id(db, warehouse_id, product_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def put_product(db: Session, warehouse_id: int, product_id: int, data: ProductCreate):
    product = get_product_by_id(db, warehouse_id, product_id)
    for key, value in data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, warehouse_id: int, product_id: int):
    product = get_product_by_id(db, warehouse_id, product_id)
    db.delete(product)
    db.commit()