def demo(*args, **kwargs):
    print('args:',args), #args collect extra arguments into tupple
    print('kwargs:',kwargs) # kwargs collect 


demo(3,4,5, name='ali',age=34)

# more complex version
 
def log_and_run(func,*args, **kwargs):
    print(f"running function {func.__name__}")
    return func(*args, **kwargs) # * means different in definition and call in call it means to make the tupple open like from (3,4)-> 3,4

def add(a,b):
    return a+b

print(log_and_run(add,3,4))