class Message:
    def __init__(self,role,content):
        self.role=role
        self.content=content

    def word_count(self):
        return len(self.content.split())

m1=Message('user','what is Rag based Models')
m2=Message('manager','Rag is Retreival Augmented Generation method used in AI')

print(m1.role)
print(m2.role)

print(m1.word_count())
    

        