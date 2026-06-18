from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer, primary_key=True, index=True)
    truck_number = Column(String, unique=True, index=True)
    plate_number = Column(String)
    status = Column(String, default="active")


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    license_number = Column(String)


class Trailer(Base):
    __tablename__ = "trailers"

    id = Column(Integer, primary_key=True, index=True)
    trailer_number = Column(String, unique=True, index=True)


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String)
    file_path = Column(String)
    document_type = Column(String, nullable=True)

    truck_id = Column(Integer, ForeignKey("trucks.id"), nullable=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    trailer_id = Column(Integer, ForeignKey("trailers.id"), nullable=True)

    date = Column(Date, nullable=True)
    vendor = Column(String, nullable=True)
    amount = Column(Float, nullable=True)
    expiry_date = Column(Date, nullable=True)
    extracted_text = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    truck_id = Column(Integer, ForeignKey("trucks.id"))
    category = Column(String)
    vendor = Column(String)
    amount = Column(Float)
    date = Column(Date)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=True)