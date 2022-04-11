from asyncpg import UniqueViolationError
from passlib.context import CryptContext
from starlette.exceptions import HTTPException

from db import database
from managers.auth import AuthManager
from models import user, counterparty

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])

        counterparty_entry = await database.fetch_one(counterparty.select().where(counterparty.c.id == user_data["counterparty_id"]))

        if not counterparty_entry:
            raise HTTPException(400, "CounterParty does not exist")

        try:
            id_ = await database.execute(user.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already exists")

        user_entry = await database.fetch_one(user.select().where(user.c.id == id_))
        return AuthManager.encode_token(user_entry)

    @staticmethod
    async def login(user_data):
        user_entry = await database.fetch_one(user.select().where(user.c.email == user_data["email"]))
        if not user_entry:
            raise HTTPException(400, "Wrong email or password")
        elif not pwd_context.verify(user_data["password"], user_entry["password"]):
            raise HTTPException(400, "Wrong email or password")
        return AuthManager.encode_token(user_entry)
