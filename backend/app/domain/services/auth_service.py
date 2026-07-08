from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.domain.repositories.user_repository import UserRepository
from app.models.user import User


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(
        self,
        email: str,
        password: str,
        full_name: str,
    ) -> User:

        existing = await self.repository.get_by_email(email)

        if existing:
            raise ValueError("User already exists")

        user = User(
            email=email,
            password_hash=hash_password(password),
            full_name=full_name,
        )

        return await self.repository.create(user)

    async def login(
        self,
        email: str,
        password: str,
    ) -> str:

        user = await self.repository.get_by_email(email)

        if user is None:
            raise ValueError("Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return create_access_token(str(user.id))