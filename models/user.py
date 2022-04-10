import sqlalchemy as sqlalchemy
from db import metadata
from models.user_role_enum import RoleType

user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255)),
    sqlalchemy.Column("first_name", sqlalchemy.String(200)),
    sqlalchemy.Column("last_name", sqlalchemy.String(200)),
    sqlalchemy.Column("phone", sqlalchemy.String(20)),
    sqlalchemy.Column("role", sqlalchemy.Enum(RoleType), nullable=False, server_default=RoleType.user.name),
    sqlalchemy.Column("counterparty_id", sqlalchemy.ForeignKey("counterparties.id"), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("modified_at", sqlalchemy.DateTime, nullable=True)
)
