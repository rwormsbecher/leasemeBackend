

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme, is_admin
from managers.lease_agreement import LeaseAgreementManager
# from schemas.request.user import UserRegisterIn, UserLoginIn
from schemas.request.lease_agreement import BaseLeaseAgreement

router = APIRouter(tags=["Lease Areements"])

@router.post("/lease_agreements/{user_id}", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=201)
async def register(request: Request, lease_agreement_data: BaseLeaseAgreement):
    user = request.state.user
    new_lease_agreement = await LeaseAgreementManager.create_lease_agreement(lease_agreement_data.dict(), user)

    return {"text": "test text"}