# list is once created and holds the older values
def add_message(msg, history=[]):
    history.append(msg)
    return history

print(add_message('hi'))
print(add_message('hello'))

#now fix by using default None Property

def fix_add_message(msg,history=None):
    if history is None:
        history=[]

    history.append(msg)
    return history

print(fix_add_message('hi fixed'))
print(fix_add_message('hello fixed'))    