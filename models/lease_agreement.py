from sqlalchemy import  Column, Integer, ForeignKey, ARRAY, Float, Boolean, DateTime
import sqlalchemy
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db import metadata

Base = declarative_base()

leaseAgreements = sqlalchemy.Table(
    "leaseagreements",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("lease_agreement_number", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("asset_ids", sqlalchemy.ARRAY(Integer), nullable=False),
    sqlalchemy.Column("total_amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("reserved_amount", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("active", sqlalchemy.Boolean, nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("modified_at", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    # sqlalchemy.Column.Relationship("invoicesgeneral", backref=True)
)

# class LeaseAgreements(Base):
#     __tablename__ = "leaseagreements"
#     id = Column(Integer, primary_key=True)
#     asset_ids = Column(ARRAY(Integer), nullable=False)
#     total_amount = Column(Float, nullable=False)
#     reserved_amount = Column(Float, nullable=False)
#     active = Column(Boolean, nullable=False)
#     created_at = Column(DateTime, server_default=sqlalchemy.func.now())
#     modified_at = Column(DateTime, nullable=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     invoices = relationship("invoicesgeneral", backref=True)
