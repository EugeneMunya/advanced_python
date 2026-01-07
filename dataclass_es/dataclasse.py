"""dataclasses provide a decorator @dataclass and fuctions to automate the creation of classes
 primarily used for storing data,significantly reducing boilerplate code"""
"""Basicaly dataclasesses are code generator that generate a standard python class"""

from functools import total_ordering
from dataclasses import asdict,astuple,dataclass,fields,KW_ONLY

class Circle:
    def __init__(self,x:int=0,y:int=0,radius:int=1):
        self._x=x
        self._y=y
        self._radius=radius

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def radius(self):
        return self._radius

    def __repr__(self):
        return f"{self.__class__.__qualname__}(x={self.x},y={self.y},radius={self.radius})"
    
    #first part
    def __eq__(self, other):
        if self.__class__==other.__class__:
            return (self.x,self.y,self.radius) == (other.x,other.y,other.radius)
        return NotImplemented
    
    def __hash__(self):
        #when objects are equals their hash should be equal too
        return hash((self.x,self.y,self.radius))
    

    #ordering implementation(override special functions such as __lt__,__le__,__gt__,__ge__)

    def __lt__(self,other):
        if self.__class__== other.__class__:
            return (self.x,self.y,self.radius)<(other.x,other.y,other.radius)
        return NotImplemented
    
    #serialization to Dictionary

    def asdict(self):
        return{'x':self.x,'y':self.y,'radius':self.radius}
    def astuple(self):
        return (self.x,self.y,self.radius)
    


#apply dataclasse decorator

@dataclass(frozen=True)
class CircleD:
    x:int=0
    y:int=0
    _:KW_ONLY
    radius:int=1




c=CircleD(1,1,radius=1)
c1=CircleD(radius=10)

print("as dict",asdict(c))
print("as tutple",astuple(c1))

for field in fields(c):
    print(field, end='\n---------------\n')


#slots limit the number of attributes a class can have

@dataclass(slots=True)
class S:
    x:int=0
    y:int=1

s=S()
s.z=20 #AttributeError: object has no attribute
print(s.z) 


@dataclass(kw_only=True) #allow key word argument only
class K:
    a:str=''
    b:int=0

k=K(a="kgl",b=1)
print(k.a)






