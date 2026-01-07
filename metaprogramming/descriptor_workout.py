"Desicriptor is an object that controls how attributes accessed,modified or deleted when use as a variable in another class"

class Mydescriptor:
    def __set_name__(self,owner,name):
        self.private=f'_{name}'

    def __get__(self,obj,obcls):
        if obj:
            return getattr(obj,self.private,None)
        return getattr(obcls,self.private,None)
    
    def __set__(self,obj,value):
        setattr(obj,self.private,value)
    
    def __delete__(self,obj):
        delattr(obj,self.private)


class Notchangeble:
    def __init__(self,value):
        self.const=value

    def __get__(self,obj,objcls):
        return self.const
    
    def __set__(self,obj,value):
        raise AttributeError("can't change the value")
    
    def __delete__(self,obj):
        return None
    

    
class A:
    beta=Mydescriptor()
    alpha=Mydescriptor()
    CONST = Notchangeble("North_East")


a=A()
a.beta=34
a.CONST="kgl" #AttributeError: can't change the value
print(a.beta)

