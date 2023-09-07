from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    license_plate: str
    height: int

class UserUpdateRequest(BaseModel):
    id: Optional[str]
    license_plate: Optional[str]
    height: Optional[int]

