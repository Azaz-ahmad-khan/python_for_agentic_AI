def generator(limit):
    n=1
    while n<=limit:
        yield n
        
        n+=1
       

for x in generator(3):
    print(x)


