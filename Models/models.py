



from pydantic import BaseModel
from datetime import date
from typing import List


class Client(BaseModel):
    client_id: int 
    name: str
    email: str
    telephone: str

class Account(BaseModel):
    acc_numb: int
    client_id: int 
    acc_type: str

class Transaction(BaseModel):
    trans_id: int
    trans_date: date
    trans_amount: float
    acc_numb: int 