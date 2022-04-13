import sqlalchemy
from sqlalchemy import Integer

from db import metadata

leaseAgreements = sqlalchemy.Table(
    "leaseagreements",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("asset_ids", sqlalchemy.ARRAY(Integer), nullable=False),
    sqlalchemy.Column("total_amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("reserved_amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("active", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("modified_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Relationship("invoicesgeneral", backref=True)
)