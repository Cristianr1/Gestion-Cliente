from typing import Dict
from pydantic import BaseModel
from typing import Optional


class EmployeeInDB(BaseModel):
    username: str
    password: str
    rol: str
    task: Optional[str] = None
    email: Optional[str]
    mobile: Optional[str]
    logged_in: bool
    name: str


database_employees = Dict[str, EmployeeInDB]

database_employees = {
    "empleado1": EmployeeInDB(**{"username": "empleado1",
                                 "password": "123456",
                                 "rol": "operator",
                                 "task":"Ir por pan",
                                 "email":"empleado1@email.com.co",
                                 "mobile":"300 123 4567",
                                 "logged_in": False,
                                 "name":"Juan Esteban Julius"}),
    "admin1": EmployeeInDB(**{"username": "admin1",
                              "password": "admin",
                              "rol": "admin",
                               "task":"Comer el pan",
                               "email":"admin@email.com.co",
                               "mobile":"300 890 1234",
                              "logged_in": False,
                              "name":"Juan Esteban Caicedo"}),
}

def get_employee(username: str):
    if username in database_employees.keys():
        return database_employees[username]
    else:
        return None


def update_employee(employee_in_db: EmployeeInDB):
    database_employees[employee_in_db.username] = employee_in_db
    return employee_in_db


def display_all():
    return database_employees
