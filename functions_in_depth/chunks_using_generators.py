def readChunk(text,size):
    for x in range(0,len(text),size):
        yield text[x:x+size]

for x in readChunk('this is first time',4):
    print(x)
