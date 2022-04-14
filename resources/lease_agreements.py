from typing import List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme, is_admin
from managers.lease_agreement import LeaseAgreementManager
# from schemas.request.user import UserRegisterIn, UserLoginIn
from schemas.request.lease_agreement import BaseLeaseAgreement
from schemas.response.lease_agreement import LeaseAgreementOut

router = APIRouter(tags=["Lease Areements"])

@router.post("/lease_agreements/{user_id}", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=201, response_model=LeaseAgreementOut)
async def register(request: Request, lease_agreement_data: BaseLeaseAgreement):
    user = request.state.user
    new_lease_agreement = await LeaseAgreementManager.create_lease_agreement(lease_agreement_data.dict(), user)

    return new_lease_agreement

@router.get("/my_lease_agreements", dependencies=[Depends(oauth2_scheme)], status_code=200, response_model=List[LeaseAgreementOut])
async def get_my_lease_agreements(request: Request):
    user = request.state.user
    my_lease_agreements = await LeaseAgreementManager.get_my_lease_agreements(user)

    return my_lease_agreements
