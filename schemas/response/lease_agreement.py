from datetime import datetime
from typing import Optional, Union

from schemas.request.lease_agreement import BaseLeaseAgreement


class LeaseAgreementOut(BaseLeaseAgreement):
    created_at: datetime
    modified_at: Union[datetime, None]