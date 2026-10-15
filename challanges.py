# counting the roles in the chat 
def count_by_role(messages):
    count={}
    for m in messages:
        role=m['role']
        count[role]=count.get(role,0)+1

    return count;    
# returning a list of questions where the role is user
def user_questions(messages):
         user_Messages=[]
         for m in messages:
             message=m['content']
             if m['role']=='user' and m['content']:
                  user_Messages.append(message)

         return user_Messages   

def add_message(role, content, history=None):
     if history is None:
          history=[]

     history.append({'role':role,'content':content})

     return history    
     
def split_conversation(messages):
     systemPrompt,*rest=messages

     return systemPrompt['content']                 


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "Retrieval-Augmentead Generation combines search with an LLM."},
    {"role": "user", "content": "Explain chunking"},
    {"role": "assistant", "content": "Chunking splits documents into smaller pieces."},
    {"role": "user", "content": ""},
    {"role": "user", "content": "What is LangGraph?"},
]
print(count_by_role(messages=messages))

print(user_questions(messages=messages))
print(add_message(role='User',content='what is pythonic loops'))
print(split_conversation(messages=messages))