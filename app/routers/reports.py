from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def get_all():
    return []
