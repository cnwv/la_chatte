from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.films import get_films, delete_films
from core.models import db_helper
from core.schemas.films import FilmsRead
from parser import Parser
from fastapi.responses import HTMLResponse
from create_fastapi_app import templates
from fastapi import Request

router = APIRouter(tags=["Films"])


@router.get("/parse_films", response_model=list[FilmsRead])
async def parse_films(session: AsyncSession = Depends(db_helper.session_getter)):
    films = await get_films(session)
    parser = Parser()
    if not films:
        parser = Parser()
        films = await parser.run(session)
    return films


@router.get("", response_model=list[FilmsRead])
async def get_all_film(session: AsyncSession = Depends(db_helper.session_getter)):
    films = await get_films(session)
    return films


@router.delete("")
async def delete_all_films(session: AsyncSession = Depends(db_helper.session_getter)):
    await delete_films(session)
