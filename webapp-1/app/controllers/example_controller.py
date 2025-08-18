from fastapi import APIRouter, Depends
from app.services.example_service import ExampleService

router = APIRouter()

@router.get("/items/{item_id}")
def get_item(item_id: int, service: ExampleService = Depends()):
    return service.get_item_details(item_id)