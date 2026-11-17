from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import create_engine,sessionmaker,Session
# from config.env_config import DATABASE_URL
from .env_config import DATABASE_URL,ENVIRONMENT
from sqlalchemy import Integer, String, Mapped, mapped_column

engine = create_async_engine(DATABASE_URL, echo=ENVIRONMENT=="local")  # Set echo to True for local development, False for production
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[str] = mapped_column(String(50), nullable=False, default=func.now)
    updated_at: Mapped[str] = mapped_column(String(50), nullable=False,default=func.now)
    

# Dependency to inject into FastAPI routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
