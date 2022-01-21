#1.Formal
#2.Actual Argument-Type below
#Position
# Keyword
#Default
#Variable Length
#------------Keyword Argument
# def person(Height,weight):
#     print("Your Height is:",Height)
#     print("Your Weight is:", weight)
# person(Height=9.8,weight=89)# Keyword Argument

#-----------Variable Length
# def sum(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
# sum(4,7,8,4,75,5)
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(4,7,8,4,75,5)