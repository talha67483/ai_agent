from pydantic import BaseModel


# class ShemaModel(BaseModel):
#     n1:int
#     n2:int

class UserData(BaseModel):
    name:str
    age:int
    