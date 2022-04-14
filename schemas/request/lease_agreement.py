from datetime import datetime
from typing import List

from pydantic import BaseModel, validator


class BaseLeaseAgreement(BaseModel):
    lease_agreement_number: int
    asset_ids: List[int]
    total_amount: float
    reserved_amount: float
    active: bool

    @validator("lease_agreement_number")
    def validate_phone(cls, v):
        integerLength = len(str(v))
        if integerLength >= 4:
            return v

        raise ValueError("Lease agreement number must be longer than 4 numbers.")

    @validator("asset_ids")
    def validate_asset_ids(cls, v):
        if not v == []:
            return v

        raise ValueError("At least one asset type must be given.")

    @validator("total_amount")
    def validate_total_value(cls, v):
        if v > 0:
            return v

        raise ValueError("Total amount must be a positive number")

    # @validator("reserved_amount")
    # def validate_total_reserved_value(cls, v, values):
    #     if values["total_amount"] >= v:
    #         return v
    #
    #     raise ValueError("Total amount must be bigger than reserved amount")


