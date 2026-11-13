class Conversation:
    def __init__(self,systemPrompt):
        self.messages=[]
        self.add('system',systemPrompt)

    def add(self,writer,prompt):
        self.messages.append({'writer':writer,'Prompt':prompt})

    def last(self):
        return self.messages[-1] if self.messages else None


chat=Conversation('You are a helpful AI')
chat.add('user','What does RAG Stand For ?')
chat.add('llm','RAG Stands for Retrival Augmented Generation')
print(chat.last())    
print(len(chat.messages))


     