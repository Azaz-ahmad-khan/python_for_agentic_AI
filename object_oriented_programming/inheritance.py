class Tool:
    def __init__(self,name,description):
        self.name=name
        self.description=description

    def run(self, **kwargs):
        raise NotImplementedError("sub classes must implement run()")

class Calculator(Tool):  
    def __init__(self):
        super().__init__('calculator','AddTwoNumbers')

    def run(self,**kwargs):
        a=kwargs['a']
        b=kwargs['b']
        return a+b

class UpperCase(Tool):
    def __init__(self):
        super().__init__('UperCase', 'Return Words in UpperCase')

    def run(self,**kwargs):
        words=kwargs['words']
        return words.upper()        

ctool=Calculator()
print(ctool.run(a=5,b=4))

upercase=UpperCase()
print(upercase.run(words='the khan is here'))