"""iterators are objects that allows you to traverse throught elements of a collection one at time"""

#for loop behinde the scene

a=iter(list(range(10)))
while True:
    try:
        v=next(a)
        print(v)
    except StopIteration:
        break

#implementing iterator
class A:
    def __init__(self,n):
        self.end=n
        self.v=-1

    def __iter__(self):
        return self
    def __next__(self):
        value=None
        if self.v>=self.end-1:
            raise StopIteration
        else:
            self.v+=1
            value=self.v
        return value


a=A(10)

for i in a:
    print(i)

#implementing generator(generators return iterator objects that you can iterate over)

def gen(n):
    for i in range(n):
        yield i

for i in gen(5):
    print(i)