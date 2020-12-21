from db.employee_db import EmployeeInDB
from db.employee_db import update_employee, get_employee, display_all
from db.customer_db import CustomerInDB
from db.customer_db import get_customer, update_customer
from models.employee_models import EmployeeLogin, EmployeeLogout, EmployeeTask
from models.customer_models import CustomerPayment
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from random import randint
from random import seed

seed(1)

api = FastAPI(
    title="Sprint 4 y 5",
    description="APIs para los módulos de empleado y cliente",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://mg-sprint3.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.post("/authentication/")
async def authentication(login: EmployeeLogin):
    employee_in_db = get_employee(login.username)
    customer_in_db = get_customer(login.username)
    
    if customer_in_db != None:
        users_in_db = customer_in_db
    elif employee_in_db != None:
        users_in_db = employee_in_db
    else:
        return {"autenticado": False, "error": "Usuario no existe"}

    if users_in_db.password == login.password:
        return {"autenticado": True, "rol": users_in_db.rol}
    else:
        return {"autenticado": False, "error": "Contraseña incorrecta"}


@api.get("/employee/data/{username}")
async def get_employee_data(username: str):
    employee_in_db = get_employee(username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return employee_in_db


@api.get("/employee/signout/{username}")
async def signout_employee(username: str):
    employee_in_db = get_employee(username)

    if employee_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    employee_in_db.logged_in = False

    update_employee(employee_in_db)

    return {"Cerrar Sesión": True}


@api.put("/employee/task/")
async def assign_task(employee_task: EmployeeTask):
    employee_in_db = get_employee(employee_task.username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    employee_in_db.task = employee_task.task
    update_employee(employee_in_db)

    return employee_in_db


@api.get("/employees/", response_model=Dict[str, EmployeeInDB])
async def find_all_employees():
    employee_db = display_all()
    return employee_db


@api.get("/customer/data/{name}")
async def get_customer_data(name: str):
    customer_in_db = get_customer(name)

    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")

    return customer_in_db


@api.put("/customer/payment/")
async def customer_payment(customer_name: CustomerPayment):
    customer_in_db = get_customer(customer_name.name)

    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")

    customer_in_db.isPayment = True
    update_customer(customer_in_db)

    return customer_in_db


@api.put("/customer/invoice/")
async def generate_invoice(customer_name: CustomerPayment):
    customer_in_db = get_customer(customer_name.name)

    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")

    customer_in_db.isPayment = False
    customer_in_db.invoice = randint(0, 1000)
    update_customer(customer_in_db)

    return customer_in_db
