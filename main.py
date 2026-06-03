from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.api.routes import warehouses, suppliers, products, inventory

app = FastAPI(title="The Inventory Project")

# permite requesturi din browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(bind=engine)

app.include_router(warehouses.router, prefix="/api/warehouses", tags=["Warehouses"])
app.include_router(suppliers.router, prefix="/api/suppliers", tags=["Suppliers"])
app.include_router(products.router, prefix="/api/warehouses/{warehouse_id}/products", tags=["Products"])
app.include_router(inventory.router, prefix="/api/warehouses/{warehouse_id}/inventory", tags=["Inventory"])

@app.get("/")
def root():
    return {"message": "buna, API-ul merge!"}