from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from api.config import cfg
engine: AsyncEngine = create_async_engine(cfg.db)