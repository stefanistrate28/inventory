from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import warehouses, suppliers, products, inventory
from app.db.seed import seed_data

# cream aplicatia
app = FastAPI(title="Inventory Management API")

# cream tabelele in baza de date
Base.metadata.create_all(bind=engine)

# adaugam date de test
seed_data()

# adaugam routes
app.include_router(warehouses.router, prefix="/api/warehouses", tags=["Warehouses"])
app.include_router(suppliers.router, prefix="/api/suppliers", tags=["Suppliers"])
app.include_router(products.router, prefix="/api/warehouses/{warehouse_id}/products", tags=["Products"])
app.include_router(inventory.router, prefix="/api/warehouses/{warehouse_id}/inventory", tags=["Inventory"])

@app.get("/")
def root():
    return {"message": "The Inventory !"}