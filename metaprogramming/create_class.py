
"""Different ways to cleate class """

#number 1

class A:
    a=1


#number2
A=type('A',(),{'a':1})
print(A.a)