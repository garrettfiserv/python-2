from dataclasses import dataclass


@dataclass(frozen=False, order=True)
class Invoice:
    invoice_id: str
    user_id: str
    amount: float
    paid: bool

    def get_info(self):
        return f"{self.invoice_id} {self.user_id} {self.amount} {self.paid}"

    def __init__(self, invoice_id, user_id, amount, paid):
        self.invoice_id = invoice_id
        self.user_id = user_id
        self.amount = amount
        self.paid = paid
