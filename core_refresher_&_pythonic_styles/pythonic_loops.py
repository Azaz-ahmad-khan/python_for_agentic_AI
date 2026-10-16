tools=['search','calculator','email']
scores=[0.9,0.2,0.4]
for i,tool in enumerate(tools,start=1):
    print(i, tool)

for tool,score in zip(tools,scores):
    print(f"{tool} {score:.0%}")    