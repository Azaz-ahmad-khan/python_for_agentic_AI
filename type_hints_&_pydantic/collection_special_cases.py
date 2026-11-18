from typing import Optional, Literal, Callable

scores: list[int]=[3,4,5,5,3,2]
config:dict[str,float]={'temprature':0.7}
point: tuple[int,int]=(3,4)

middlename: str |None=None
role:Literal['user','manager','llm']='user'
handler:Callable[[int,int],int]