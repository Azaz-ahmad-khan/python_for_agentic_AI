class Conversation:
    def __init__(self):
        self.messages=[]

    def add(self,role,prompt):
        self.messages.append({'role':role,'Prompt':prompt})

    def last(self):
        return self.messages[-1]
    def __len__(self):
        return len(self.messages)
    def __repr__(self):                     # what print() and the debugger show
        return f"Conversation({len(self)} messages)"

chat =Conversation()
chat.add('user',"Hi there")
chat.add('llm','Hello, How Can I help YOu')
print(len(chat))    
print(chat)