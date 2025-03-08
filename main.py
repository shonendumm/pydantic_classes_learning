from pydantic import BaseModel
from dataclasses import dataclass

class User(BaseModel):
    # these are instance vars, not class vars
    id: int
    name: str
    age: int

class User_wo_pydantic:
    def __init__(self, id, name, age):
        self.id: int = id
        self.name: str = name
        self.age: int = age

@dataclass
class User_dataclass:
    # these are instance vars, not class vars
    id: int
    name: str
    age: int



user = User(id='1', name="Soohian", age="45")
print(" ")
print("user with pydantic:", user)
print("their id type is:", type(user.id)) # has coercion of input to correct type

user_wo = User_wo_pydantic(id='1', name="Soohian", age="45")
print(" ")
print("user without pydantic:", user_wo)
print("their id type is:", type(user_wo.id)) # no type coercion


user_dataclass = User_dataclass(id='1', name="Soohian", age="45")
print(" ")
print("user without pydantic:", user_dataclass)
print("their id type is:", type(user_dataclass.id)) # no type coercion