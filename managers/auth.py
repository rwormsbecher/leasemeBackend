import http
from datetime import datetime, timedelta
from http.client import HTTPException
from typing import Optional

import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from db import database
from models import user, RoleType
import os


jwt_secret = os.environ.get('jwt_secret', 'jjkassajkasjkasjka')

class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user["id"],
                "exp": datetime.utcnow() + timedelta(minutes=120)
            }
            return jwt.encode(payload, jwt_secret,  algorithm="HS256")
        except Exception as ex:
            raise ex


class CustomHttpBearer (HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)
        try:
            # Decode the token and set the user data to the request method for easier future access.
            payload = jwt.decode(res.credentials, jwt_secret, algorithms=['HS256'])

            user_data = await database.fetch_one(user.select().where(user.c.id == payload["sub"]))
            request.state.user = user_data
            return user_data
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token is expired")
        except Exception:
            raise HTTPException(401, "Token is invalid")

oauth2_scheme = CustomHttpBearer()

def is_admin(request: Request):
    if not request.state.user["role"] == RoleType.admin:
        raise HTTPException(403, "Forbidden")
