class Agent:
    framwork='Custom'
    def __init__(self,name):
        self.name=name

a=Agent('planner')
b=Agent('Writer')

print(a.framwork,b.framwork) # same framwork name as that is class attribute
print(a.name,b.name) # different as they are instance attributes.


