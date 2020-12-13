from db.employee_db import EmployeeInDB
from db.employee_db import update_employee, get_employee
from models.employee_models import EmployeeLogin, EmployeeLogout, EmployeeTask
from fastapi import FastAPI, HTTPException

api = FastAPI(
    title="Sprint 2",
    description="APIs para el modulo de empleado",
    version="0.0.1",
)

#ES UNA PRUEBA
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
    employee_in_db.logged_in = False

    update_employee(employee_in_db)

    return {"Cerrar Sesión": True}

#Comentario
@api.put("/employee/task/")
async def assign_task(employee_task: EmployeeTask):
    employee_in_db = get_employee(employee_task.username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    employee_in_db.task = employee_task.task
    update_employee(employee_in_db)

    return employee_in_db
