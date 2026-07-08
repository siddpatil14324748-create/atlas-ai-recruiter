from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import ALGORITHM, SECRET_KEY
from app.database.session import get_db
from app.models.user import User
from sqlalchemy import select


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(lambda: None),
):
    raise NotImplementedError("Will be implemented in the next step.")