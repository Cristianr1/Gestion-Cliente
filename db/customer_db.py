from typing import Dict
from pydantic import BaseModel

class CustomerInDB(BaseModel):
    id_customer : int
    username: str
    password: str
    address: str
    invoice: int
    isPayment: bool
    rol: str
    email: str
    mobile: str

database_customers = Dict[str, CustomerInDB]

database_customers = {
    "Multidimensionales": CustomerInDB(**{"id_customer": 1000,
                                        "username": "Multidimensionales",
                                        "password": "123456",
                                        "address": "Bogotá",
                                        "invoice" : 125,
                                        "isPayment": True,
                                        "rol": "Cliente",
                                        "email":"multidim@gmail.com",
                                        "mobile":"320 221 5254",
                                        }),
    
    "Fepco": CustomerInDB(**{"id_customer": 1001,
                            "username": "Fepco",
                            "password": "654321",
                            "address": "Bogotá",
                            "invoice" : 131,
                            "isPayment": False,
                            "rol": "Cliente",
                            "email":"fepco@gmail.com",
                            "mobile":"310 891 2234",
                                        }),

    "Indumil": CustomerInDB(**{"id_customer" : 1002,
                            "username": "Indumil",
                            "password": "qwerty",
                            "address": "Soacha",
                            "invoice" : 186,
                            "isPayment": False,
                            "rol": "Cliente",
                            "email":"indumil@gmail.com",
                            "mobile":"311 821 9239",
                                        })
}

def get_customer(name: str):
    if name in database_customers.keys():
        return database_customers[name]
    else:
        return None

def update_customer(customer_in_db: CustomerInDB):
    database_customers[customer_in_db.username] = customer_in_db
    return customer_in_db

