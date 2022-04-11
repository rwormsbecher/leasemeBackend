from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str


class UserRegisterIn(BaseUser):
    password: str
    phone: str
    first_name: str
    last_name: str
    counterparty_id: int


class UserLoginIn(BaseUser):
    password: str

