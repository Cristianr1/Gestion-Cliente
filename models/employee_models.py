from pydantic import BaseModel


class EmployeeLogin(BaseModel):
    username: str
    password: str


class EmployeeLogout(BaseModel):
    username: str
    logged_in: bool


class EmployeeTask(BaseModel):
    username: str
    task: str
