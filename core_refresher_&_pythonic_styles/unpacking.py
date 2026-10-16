
#swapping without requiring the temp variable.
a,b =1,2
a,b=b,a

#the first index is assigned to variable->first
#the last index is assigned to variable->last
#all the remaining portion in the middle is assigned to the vaiable middle which is called unpacking

first,*middle,last=[1,2,3,4,5,6,7,8,9,10]
print(first)
print(last)
print(middle)

#• he ** operator unpacks the key-value pairs from a dictionary. By placing both inside a new dictionary literal {...}, Python merges them together.
# The rule of duplicate keys: When keys overlap (like "temperature" in this example), Python processes them from left to right. The last dictionary specified wins, meaning the values in overrides overwrite the values in defaults.
# The result: config becomes {'temperature': 0.2, 'max_tokens': 500}.
default={'temprature':0.7, 'max_tokens':5000}
override={'temprature':0.2}
config={**default,**override}
print(config)