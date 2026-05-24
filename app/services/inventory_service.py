from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.inventory import InventoryMovement, MovementType
from app.models.product import Product
from app.schemas.inventory import MovementCreate

def get_inventory(db: Session, warehouse_id: int):
    
    return db.query(Product).filter(Product.warehouse_id == warehouse_id).all()

def get_movements(db: Session, warehouse_id: int, product_id: int):
 
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.warehouse_id == warehouse_id
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produsul nu a fost gasit")
    
    return db.query(InventoryMovement).filter(
        InventoryMovement.product_id == product_id
    ).all()

def stock_in(db: Session, warehouse_id: int, product_id: int, data: MovementCreate):
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.warehouse_id == warehouse_id
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produsul nu a fost gasit")
    
    # adaugam stoc
    product.stock_quantity += data.quantity
    
    movement = InventoryMovement(
        product_id=product_id,
        movement_type=MovementType.STOCK_IN,
        quantity=data.quantity,
        notes=data.notes
    )
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement

def stock_out(db: Session, warehouse_id: int, product_id: int, data: MovementCreate):
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.warehouse_id == warehouse_id
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produsul nu a fost gasit")
    
    if product.stock_quantity < data.quantity:
        raise HTTPException(status_code=400, detail="Stoc insuficient")
    
    product.stock_quantity -= data.quantity
    
    movement = InventoryMovement(
        product_id=product_id,
        movement_type=MovementType.STOCK_OUT,
        quantity=data.quantity,
        notes=data.notes
    )
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement

def transfer(db: Session, warehouse_id: int, product_id: int, data: MovementCreate):
    product = db.query(Product).filter(
        Product.id == product_id,
        Product.warehouse_id == warehouse_id
    ).first()
    if not product:
        raise HTTPException(status_code=404, detail="Produsul nu a fost gasit")
    
    movement = InventoryMovement(
        product_id=product_id,
        movement_type=MovementType.TRANSFER,
        quantity=data.quantity,
        notes=data.notes
    )
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement