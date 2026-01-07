"""metaclass is a class that create class objet from the user defined class, Our defined classes are recipes that meta class uses to create class represation in memory"""



class Meta(type):
    @staticmethod
    def __new__(clobj,cls,base,att,*args,**kwargs):
        d={}
        for k,v in att.items():
            if not k.startswith('__'):
                d[k.upper()]=v
        
        d['mylist']=list(range(d['B']))
        return super(Meta,Meta).__new__(clobj,cls,base,d,*args,**kwargs)
    

class A(metaclass=Meta):
    b=10

li=iter(A.mylist)

while True:
    try:
        print(next(li))
    except StopIteration:
        break

print(A.__dict__)
