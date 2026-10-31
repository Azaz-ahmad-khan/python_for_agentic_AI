def add(a,b): return a+b
def multiply(a,b):return a*b

tools={'add':add,'multiply':multiply}
tools_name='multiply'
call_tool=tools[tools_name](5,4)
print(call_tool)