from pydantic import BaseModel

class User(BaseModel):
    # these are instance vars, not class vars
    id: int
    name: str
    age: int

class User_wo_pydantic():
    def __init__(self, id, name, age):
        self.id: int = id
        self.name: str = name
        self.age: int = age


user = User(id='1', name="Soohian", age="45")
print(" ")
print("user with pydantic:", user)
print("their id type is:", type(user.id))

user_wo = User_wo_pydantic(id='1', name="Soohian", age="45")
print(" ")
print("user without pydantic:", user_wo)
print("their id type is:", type(user_wo.id))