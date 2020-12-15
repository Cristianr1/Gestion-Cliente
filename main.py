from db.employee_db import EmployeeInDB
from db.employee_db import update_employee, get_employee, display_all
from models.employee_models import EmployeeLogin, EmployeeLogout, EmployeeTask
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

api = FastAPI(
    title="Sprint 2",
    description="APIs para el modulo de empleado",
    version="0.0.1",
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ES UNA PRUEBA
@api.post("/employee/auth/")
async def auth_employee(employee_login: EmployeeLogin):
    employee_in_db = get_employee(employee_login.username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El empleado no existe")

    if employee_in_db.password != employee_login.password:
        return {"Autenticado": False}
    else:
        employee_in_db.logged_in = True
        update_employee(employee_in_db)
        return {"Autenticado": True}


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


# Comentario
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
