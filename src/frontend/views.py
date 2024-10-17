from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from create_fastapi_app import templates

router = APIRouter(tags=["frontend"])


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
