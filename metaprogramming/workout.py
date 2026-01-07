import inspect


#singleton pattern using metaprogramming

class Singleton(type):
    def __call__(self, *args, **kwds):
        if not hasattr(Singleton.__call__,'single_obj'):
            setattr(Singleton.__call__,'single_obj',super(Singleton,self).__call__(*args,**kwds))
        return getattr(Singleton.__call__,'single_obj')
    

class T(metaclass=Singleton):
    pass


k=T()
l=T()
m=T()

#only one instance was used
print(id(k))#139961716797840
print(id(l))#139961716797840
print(id(m))#139961716797840
print("----------------")


class R:
    pass


x=R()
y=R()
z=R()

#every call create separate instance
print(id(x))#139961716797888
print(id(y))#139961716795392
print(id(z))#139961716795440


#limiting the number of attributes a instance can have with meta programming
class Meta(type):
    @staticmethod
    def __new__(clsobj,cls,base,dct,*args,**kwds):
        if "__init__" in dct:
            slots=tuple(inspect.signature(dct["__init__"]).parameters.keys())[1:]
            print(slots)
            dct['__slots__']= slots
        return super().__new__(clsobj,cls,base,dct,*args,**kwds)


class A(metaclass=Meta):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

inst = A(400,500,600)
print(A.__dict__)

#we nolonger have instance __dict__ method and we are not allowed to add an attribute on the instance
#print(inst.__dict__) this error

