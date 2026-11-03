#decorators are functions that take functions and return improved ones
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with args {args} and {kwargs}")
        result=func(*args, **kwargs)
        print(result)
        return result
    return wrapper
@log_call
def add(a,b):
    return a+b
add(3,4)

# this is basically used when you want to perform more tasks while executing a specific function
# here you can see we print the name of function and the arguments of the function which is being called.