import re

from email_validator import validate_email as validate_e, EmailNotValidError
from pydantic import BaseModel, validator


class BaseUser(BaseModel):
    email: str

    @validator("email")
    def validate_email(cls, v):
        try:
            validate_e(v)
            return v
        except EmailNotValidError:
            raise ValueError("Invalid email")


class UserRegisterIn(BaseUser):
    password: str
    phone: str
    first_name: str
    last_name: str
    counterparty_id: int

    @validator("phone")
    def validate_phone(cls, v):
        try:

            result = bool(re.search("^[+\0-9]+$", v))
            if  result:
                return v

            raise ValueError("Phone can only consist out of numers and a '+' sign")

        except ValueError:
            raise ValueError("Phone can only consist out of numers and a '+' sign")

class UserLoginIn(BaseUser):
    password: str


