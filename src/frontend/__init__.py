from fastapi import APIRouter
from frontend.views import router as index_router

router = APIRouter()

router.include_router(index_router)
