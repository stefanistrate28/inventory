from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import warehouses, suppliers, products, inventory
from fastapi.staticfiles import StaticFiles

# cream aplicatia
app = FastAPI(title="The Inventory Proiect")
app.mount("/static", StaticFiles(directory="static"), name="static")

# cream tabelele in baza de date
Base.metadata.create_all(bind=engine)



# adaugam routes
app.include_router(warehouses.router, prefix="/api/warehouses", tags=["Warehouses"])
app.include_router(suppliers.router, prefix="/api/suppliers", tags=["Suppliers"])
app.include_router(products.router, prefix="/api/warehouses/{warehouse_id}/products", tags=["Products"])
app.include_router(inventory.router, prefix="/api/warehouses/{warehouse_id}/inventory", tags=["Inventory"])

@app.get("/")
def root():
    return {"message": "The Inventory !"}