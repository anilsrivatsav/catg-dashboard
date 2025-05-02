from sqlalchemy.orm import Session
from app.models.payments import Payment
from app.models.stalls import Stall
from app.schemas.payments import PaymentCreate
from fastapi import HTTPException, status

def get_payments(db: Session):
    return db.query(Payment).all()

def create_payment(db: Session, payment: PaymentCreate):
    # Check if the stall (unit_no) exists
    stall = db.query(Stall).filter(Stall.unit_no == payment.unit_no).first()
    if not stall:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Stall with unit_no {payment.unit_no} does not exist."
        )
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment
def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()
def update_payment(db: Session, payment_id: int, payment: PaymentCreate):   
    db_payment = get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with id {payment_id} not found."
        )
    # Check if the stall (unit_no) exists
    stall = db.query(Stall).filter(Stall.unit_no == payment.unit_no).first()
    if not stall:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Stall with unit_no {payment.unit_no} does not exist."
        )
    for key in payment.dict().keys():
        setattr(db_payment, key, payment[key])
    db.commit()
    return db_payment
def delete_payment(db: Session, payment_id: int):   
    db_payment = get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Payment with id {payment_id} not found."
        )
    # Check if the stall
    stall = db.query(Stall).filter(Stall.unit_no == db_payment.unit_no).first()
    if not stall:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Stall with unit_no {db_payment.unit_no} does not exist."
        )
    db.delete(db_payment)
    db.commit() 