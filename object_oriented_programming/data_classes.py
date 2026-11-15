from dataclasses import dataclass, field
@dataclass
class Message:
    role: str
    content: str
    tokens: int=0

#Many classes only exist to hold data. Writing __init__ and __repr__ by hand each time is tedious, so @dataclass generates them.
@dataclass
class Session:
    user_id:str
    message: list=field(default_factory=list) # safe way to default to empty list when new conversation starts


m=Message('user','hi')
print(m)    

s1=Session('u1')
s1.message.append(m)
s2=Session('u2')
print(s1.message)
print(s2.message)

