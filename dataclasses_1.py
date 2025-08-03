from dataclasses import dataclass
from pydantic import BaseModel,ConfigDict

# @dataclass
# class Car:
#     name:str
#     model:int




class Car(BaseModel):
    name:str
    model:int
    
    class Config:
        validate_assignment = True 


def get_car(car:Car):
    car.name = 123
    print(car.name)
    print(car.model)



c1  = Car(name="corolla",model=2020)

get_car(c1)

