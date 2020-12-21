from pydantic import BaseModel

class CustomerPayment(BaseModel):
    name: str
