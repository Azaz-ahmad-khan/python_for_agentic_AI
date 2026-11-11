def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"calling the function {func.__name__}")
        print(f"with argurments {args}, {kwargs}")
        result=func(*args,**kwargs)
        print(f"result is {result}")
        return result
    return wrapper
@decorator
def add(a,b):
    return a+b

add(2,3)