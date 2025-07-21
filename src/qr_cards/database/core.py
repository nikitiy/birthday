from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase

from qr_cards.database.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_db)]


class Base(DeclarativeBase):
    pass
