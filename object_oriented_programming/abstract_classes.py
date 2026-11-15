from abc import ABC, abstractmethod
class BaseTool(ABC):
    @abstractmethod
    def run(self,**kwargs):
        ...
class Echo(BaseTool):
    def run(self,**kwargs):
        text=kwargs['text']
        return text

class BrokenTool(BaseTool):
    pass


Echo()
#BrokenTool() does not work because the abstract method is not implemented.