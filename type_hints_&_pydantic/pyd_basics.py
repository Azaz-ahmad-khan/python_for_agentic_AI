from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int
    email:str|None=None

u=User(name='Azaz',age=34,email='azazahamdkhan264@gmail.com')
print(u)
print(u.name)
print(u.email)

u1=User(name='Ali',age=20)
print(u1)
print(u1.email)    