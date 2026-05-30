from app.db.database import SessionLocal
from app.models.warehouse import Warehouse
from app.models.supplier import Supplier
from app.models.product import Product

def seed_data():
    db = SessionLocal()

    
    exista_date = db.query(Warehouse).first()
    if exista_date:
        print("Datele exista deja in baza de date, nu mai adaugam nimic")
        db.close()
        return

    print("Adaugam date in baza de date...")


    depozit1 = Warehouse(
        name="Depozit Cluj",
        location="Cluj-Napoca, Strada Fabricii 10",
        description="Depozitul principal din Cluj"
    )

    depozit2 = Warehouse(
        name="Depozit Bucuresti",
        location="Bucuresti, Strada Industriei 5",
        description="Depozitul din Bucuresti"
    )

    depozit3 = Warehouse(
        name="Depozit Timisoara",
        location="Timisoara, Strada Logofat 3",
        description="Depozitul din Timisoara"
    )

    db.add(depozit1)
    db.add(depozit2)
    db.add(depozit3)
    db.commit()

    db.refresh(depozit1)
    db.refresh(depozit2)
    db.refresh(depozit3)

    print("Warehouse-urile au fost adaugate!")


    supplier1 = Supplier(
        name="Samsung Romania",
        contact_email="contact@samsung.ro",
        phone="0700 111 222",
        address="Bucuresti, Sector 1"
    )

    supplier2 = Supplier(
        name="Apple Romania",
        contact_email="contact@apple.ro",
        phone="0700 333 444",
        address="Bucuresti, Sector 2"
    )

    supplier3 = Supplier(
        name="LG Electronics",
        contact_email="contact@lg.ro",
        phone="0700 555 666",
        address="Cluj-Napoca, Centru"
    )

    db.add(supplier1)
    db.add(supplier2)
    db.add(supplier3)
    db.commit()

    db.refresh(supplier1)
    db.refresh(supplier2)
    db.refresh(supplier3)

    print("Supplier-ii au fost adaugati!")


    produs1 = Product(
        name="Samsung Galaxy S24",
        sku="SAM-S24-BLK",
        description="Telefon Samsung Galaxy S24 negru",
        price=3500.0,
        stock_quantity=50,
        warehouse_id=depozit1.id,
        supplier_id=supplier1.id
    )

    produs2 = Product(
        name="Samsung Galaxy S24 Ultra",
        sku="SAM-S24U-BLK",
        description="Telefon Samsung Galaxy S24 Ultra negru",
        price=5500.0,
        stock_quantity=30,
        warehouse_id=depozit1.id,
        supplier_id=supplier1.id
    )

    produs3 = Product(
        name="iPhone 15",
        sku="APL-IP15-BLK",
        description="Telefon Apple iPhone 15 negru",
        price=5000.0,
        stock_quantity=25,
        warehouse_id=depozit1.id,
        supplier_id=supplier2.id
    )


    produs4 = Product(
        name="iPhone 15 Pro",
        sku="APL-IP15P-BLK",
        description="Telefon Apple iPhone 15 Pro negru",
        price=7000.0,
        stock_quantity=15,
        warehouse_id=depozit2.id,
        supplier_id=supplier2.id
    )

    produs5 = Product(
        name="LG TV 55 inch",
        sku="LG-TV55-BLK",
        description="Televizor LG 55 inch 4K",
        price=2800.0,
        stock_quantity=20,
        warehouse_id=depozit2.id,
        supplier_id=supplier3.id
    )

    produs6 = Product(
        name="Samsung TV 65 inch",
        sku="SAM-TV65-BLK",
        description="Televizor Samsung 65 inch 4K",
        price=4200.0,
        stock_quantity=10,
        warehouse_id=depozit2.id,
        supplier_id=supplier1.id
    )

    produs7 = Product(
        name="LG Monitor 27 inch",
        sku="LG-MON27-BLK",
        description="Monitor LG 27 inch Full HD",
        price=1200.0,
        stock_quantity=35,
        warehouse_id=depozit3.id,
        supplier_id=supplier3.id
    )

    produs8 = Product(
        name="Samsung Monitor 24 inch",
        sku="SAM-MON24-BLK",
        description="Monitor Samsung 24 inch Full HD",
        price=900.0,
        stock_quantity=40,
        warehouse_id=depozit3.id,
        supplier_id=supplier1.id
    )

    db.add(produs1)
    db.add(produs2)
    db.add(produs3)
    db.add(produs4)
    db.add(produs5)
    db.add(produs6)
    db.add(produs7)
    db.add(produs8)
    db.commit()

    print("Produsele au fost adaugate!")
    print("Toate datele au fost adaugate cu succes!")

    db.close()