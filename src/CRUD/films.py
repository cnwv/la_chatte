from typing import Sequence

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Film
from core.models.db_helper import db_helper


async def get_films(
    session: AsyncSession,
) -> Sequence[Film]:
    stmt = select(Film)
    result = await session.scalars(stmt)
    return result.all()


async def create_film(
    data: dict,
):
    async with db_helper.session_factory() as session:
        film: Film = Film(**data)
        session.add(film)
        await session.commit()
        return film


async def delete_films(session: AsyncSession):
    stmt = delete(Film)
    await session.execute(stmt)
    await session.commit()
    return 200
