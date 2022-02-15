# Pass by value & pass by reference (in python we don't have this method)
# def update(x):
#     print(id(x))
#     x=2
#     print(id(x))
#     print("X is",x)
# a=10
# print(id(a))
# update(a)
# print("a is",a)

#Keyword Arguments
def person(name,age):
    print(name)
    print(age+5)
person(name='sagar',age=25) # This is called Keyword arguments
# Position Arguments
def person1(name,age):
    print(name)
    print(age)
person1('Shanya',20)
#Default Arguments
def Facebook(name,age=18):
    print(name)
    print(age)
Facebook('Sagar',30) # if we pass the value while calling the function it will override the value when it gets call.

#Variable Length

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
# Here *b will accept the multiple value when user enter but it ll create tuple
sum(2,45,7,5,75,457,2421,2)
#ANOTHER EXAMPLE
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
# Here *b will accept the multiple value when user enter but it ll create tuple
sum(2,45,7,5,75,457,2421,2)
