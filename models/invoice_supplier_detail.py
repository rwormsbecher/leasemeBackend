import sqlalchemy

from db import metadata

invoice_supplier_Detail = sqlalchemy.Table(
    "invoicesupplierdetails",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("chamber_of_commerce_registration_number", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("vat_id", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("phone", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("iban", sqlalchemy.String, nullable=False),

)