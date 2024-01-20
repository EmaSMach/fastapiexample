from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int = None
    address: str = None
    phone: str = None
    email: str = None
    password: str = None
