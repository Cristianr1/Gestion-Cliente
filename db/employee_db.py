from typing import Dict
from pydantic import BaseModel
from typing import Optional


class EmployeeInDB(BaseModel):
    username: str
    password: str
    rol: str
    task: Optional[str] = None
    logged_in: bool


database_employees = Dict[str, EmployeeInDB]

database_employees = {
    "empleado1": EmployeeInDB(**{"username": "empleado1",
                                 "password": "123456",
                                 "rol": "operator",
                                 "logged_in": False}),
}


def get_employee(username: str):
    if username in database_employees.keys():
        return database_employees[username]
    else:
        return None


def update_employee(employee_in_db: EmployeeInDB):
    database_employees[employee_in_db.username] = employee_in_db
    return employee_in_db
