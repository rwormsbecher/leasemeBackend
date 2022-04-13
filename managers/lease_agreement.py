from starlette.exceptions import HTTPException

from db import database
from models import lease_agreement, leaseAgreements


class LeaseAgreementManager:

    @staticmethod
    async def create_lease_agreement(lease_agreement_data, user):
        lease_agreement_data["user_id"] = user["id"]

        try:
            new_lease_agreement_id = await database\
                .execute(leaseAgreements
                         .insert()
                         .values(lease_agreement_data))

            new_lease_agreement = await database\
                .fetch_one(leaseAgreements
                           .select()
                           .where(leaseAgreements.c.id == new_lease_agreement_id))
        except Exception:
            raise HTTPException(400, "Somethign went wrong creating the lease agreement.")

        return new_lease_agreement