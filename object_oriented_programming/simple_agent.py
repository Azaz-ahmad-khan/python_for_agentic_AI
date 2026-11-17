class calculatorTool:
    name='Calculator'
    def run(self,**kwargs):
        a=kwargs['a']
        b=kwargs['b']
        return a+b

class UperCaseTool:
    name='Upper case'
    def run(self,**kwargs):
        word=kwargs['words']
        return word.upper()

class SimpleAgent:
    def __init__(self,name,tools):
        self.name=name
        self.tools={t.name: t for t in tools}
        self.history=[]

    def useAgent(self,name,**kwargs):
        if name not in self.tools:
            return f"unknown tool {name}"
        result =self.tools[name].run(**kwargs)        
        return result
    
agent=SimpleAgent('helper',[calculatorTool(),UperCaseTool()])


print(agent.useAgent('Calculator',a=5,b=3))
print(agent.useAgent('Upper case',words='hi there'))