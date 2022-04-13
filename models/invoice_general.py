import sqlalchemy

from db import metadata
from models.invoice_status_enum import InvoiceStatus

invoice_general = sqlalchemy.Table(
    "invoicesgeneral",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("invoice_number", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("invoice_date", sqlalchemy.DateTime, nullable=False),
    sqlalchemy.Column("interest_rate", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("vat_value", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("free_of_vat", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(InvoiceStatus), server_default=InvoiceStatus.initial.name),
    sqlalchemy.Column("step_left_off", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("created_by", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("modified_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("modified_by", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("invoice_supplier_details_id", sqlalchemy.ForeignKey("invoicesupplierdetails.id")),
    sqlalchemy.Column("lease_agreement_id", sqlalchemy.ForeignKey("leaseagreements.id"))

)