import sqlalchemy

counterparty = sqlalchemy.Table(
    "counterparty",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(120), nullable=False),
    sqlalchemy.Column("verified", sqlalchemy.Boolean, nullable=False, server_default=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("modified_at", sqlalchemy.DateTime, nullable=True),
)