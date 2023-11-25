from pydantic import BaseModel


class RegisterSchema(BaseModel):
    username:str
    password:str
    class Config:
        strict= True

class ChangePasswordSchema(BaseModel):
    username:str
    old_password:str
    new_password:str
    class Config:
        strict= True

    