def call_llm(prompt,model='Demo-model',temprature=0.7):
    return f"{model} @ {temprature} {prompt}"

print( call_llm('hi') )# uses both default
print(call_llm('hello', temprature=0.3)) #key word aruguments:say which one you set
print(call_llm(model='gpt-mini',prompt='hello there')) # arguments can be in any order

