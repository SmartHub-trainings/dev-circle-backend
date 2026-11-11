from pydantic import BaseModel, EmailStr, Field
from typing  import Literal

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role:Literal['learner', 'engineer'] = 'user'
    password: str
    bio:str
    profession:str
