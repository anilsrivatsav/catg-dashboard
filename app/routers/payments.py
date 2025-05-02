from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.payments import Payment, PaymentCreate
from app.services.payment_service import (
    get_payments, create_payment, get_payment, update_payment, delete_payment
)
from app.models.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Payment])
def read_payments(db: Session = Depends(get_db)):
    return get_payments(db)

@router.post("/", response_model=Payment, status_code=status.HTTP_201_CREATED)
def add_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return create_payment(db, payment)

@router.get("/{payment_id}", response_model=Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.put("/{payment_id}", response_model=Payment)
def update_payment_endpoint(payment_id: int, payment: PaymentCreate, db: Session = Depends(get_db)):
    return update_payment(db, payment_id, payment)

@router.delete("/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment_endpoint(payment_id: int, db: Session = Depends(get_db)):
    delete_payment(db, payment_id)
    return
