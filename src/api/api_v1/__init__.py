from fastapi import APIRouter

# from api.api_v1.auth.auth import router as demo_auth_router
from core.config import settings

from api.api_v1.pub.films import router as cinema

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    cinema,
    prefix=settings.api.v1.films,
)

