
# a=4 # Global variable
# def some():
#     a=10 # Local variable
#     print("Inside of Function",a)
# some()
#
# print("Outside of Function",a)

#-----global keyword
a=1
# print(id(a))
def fun():
    # global a
    x=globals()['a'] # how to change outside a value in want to access also local variable
    globals()['a']=20
    print(x)
    a=2
    print("Channing the value of outside of function:",a)
fun()

print("outside",a)