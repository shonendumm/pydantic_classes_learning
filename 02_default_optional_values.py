from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    blk: Optional[int]
    street: str

class User(BaseModel):
    id: int
    name: str
    address: Address


user = User(id=1, name="Soo", address=dict(blk=1, street="AMK"))
print('+' * 10)
print('')
print(user)
print(user.model_dump()) # convert to dictionary
print(user.model_dump_json()) # serialization to JSON string
print('')
print('+' * 10)

# get property value
address = user.address
print("The street is", address.street)