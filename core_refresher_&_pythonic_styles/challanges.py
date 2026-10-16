# counting the roles in the chat 
def count_by_role(messages):
    count={}
    for m in messages:
        role=m['role']
        count[role]=count.get(role,0)+1

    return count  
# returning a list of questions where the role is user
def user_questions(messages):
         user_Messages=[]
         for m in messages:
            
             if m['role']=='user' and m['content']:
                  user_Messages.append(m['content'])

         return user_Messages   
# adding messages of user or system to the history
def add_message(role, content, history=None):
     if history is None:
          history=[]

     history.append({'role':role,'content':content})

     return history    
# spliting conversation using star unpacking     
def split_conversation(messages):
     systemPrompt,*rest=messages

     return systemPrompt['content'],rest                 

def format_transcript(messages):
     lines=[]
     for i, m in enumerate(messages,start=1):
          content=m['content'] or "(empty)"
          if len(content)>30:
               content= content[:30] +"..."
          lines.append(f"{i}. [{m['role'].upper()}] {content}")

     return  lines

def merge_config(defaults, overrides):
      return {**defaults,**overrides}
    

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
print(add_message(role='user',content='what is pythonic loops'))
print(split_conversation(messages=messages))
print(format_transcript(messages=messages))

print(merge_config(defaults = {"temperature": 0.7, "max_tokens": 500, "model": "demo"},
overrides = {"temperature": 0.2}))