from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str | None = None
    age: int | None = None
    address: str | None = None
    phone: str | None = None
    email: str | None = None
    password: str | None = None
