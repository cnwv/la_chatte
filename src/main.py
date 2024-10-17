import uvicorn

from api import router as api_router
from frontend import router as frontend_router
from core.config import settings
from create_fastapi_app import create_app
from fastapi.middleware.cors import CORSMiddleware

main_app = create_app(
    create_custom_static_urls=True,
)

main_app.include_router(api_router)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000/",
        "https://la-chatte.dev-cnwv.ru",
        "http://localhost:8000",
        "http://0.0.0.0:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(frontend_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
