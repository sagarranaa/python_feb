# Fibonacci series
# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(6)
# Fibonacci series
def fib(x):
    a=0
    b=1
    if x<=0:
        print("in valid")
    elif x==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            a=b
            b=c
            if(c<=x):
                print(c)
x=int(input("enter the number of values"))
fib(x)
