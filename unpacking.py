
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


default={'temprature':0.7, 'max_tokens':5000}
override={'temprature':0.2}
config={**default,**override}
print(config)