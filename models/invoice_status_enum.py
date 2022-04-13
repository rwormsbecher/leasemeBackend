import enum

class InvoiceStatus(enum.Enum):
    initial = "initial"
    pending = "pending"
    waiting_for_apporval = "waitingForApproval"
    approved = "approved"
    approved_twice = "approved_twice"
    completed = "complated"
    paid_out = "paidOut"
    