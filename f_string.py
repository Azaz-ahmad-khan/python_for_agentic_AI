name,tokens,cost='gpt-demo',1523,0.0123
print(f"model: {name} , tokens: {tokens}, cost: {cost:.4f}")

question='what is langraph'
prompt=f'''
 you are a tutor:
 Answer Clearly

 Question: {question}

'''