from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from fastapi import UploadFile, File
import os
import models

app = FastAPI(title="FleetDoc AI Backend")

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FleetDoc AI backend is running"}


@app.post("/trucks")
def create_truck(truck_number: str, plate_number: str, status: str = "active", db: Session = Depends(get_db)):
    truck = models.Truck(
        truck_number=truck_number,
        plate_number=plate_number,
        status=status
    )
    db.add(truck)
    db.commit()
    db.refresh(truck)
    return truck


@app.get("/trucks")
def get_trucks(db: Session = Depends(get_db)):
    return db.query(models.Truck).all()


@app.post("/drivers")
def create_driver(name: str, license_number: str, db: Session = Depends(get_db)):
    driver = models.Driver(name=name, license_number=license_number)
    db.add(driver)
    db.commit()
    db.refresh(driver)
    return driver


@app.get("/drivers")
def get_drivers(db: Session = Depends(get_db)):
    return db.query(models.Driver).all()

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):
    
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "file_name": file.filename,
        "file_path": file_path
    }