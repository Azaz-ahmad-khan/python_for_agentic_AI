messages = [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "Explain agents"},
]

user_text=[m['content'] for m in messages if m['role']=='user' ]
print(user_text)
#Rule of thumb: if a comprehension needs more than one if or nested loops and stops being readable, use a normal for loop.