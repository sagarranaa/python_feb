# Program to make simple calculator using Functions
#Define the functioins

def add(x,y):
    """" This functions add 2 numbers"""
    return x+y

def substract(x,y):
    """" This functions subtract 2 numbers """
    return x-y

def multiple(x,y):
    """" This functions multiplies 2 numbers """
    return x*y

def devide(x,y):
    """" This functions divides 2 numbers"""
    return x/y

def power(x,y):
    """" This functions works for power """
    return pow(x,y)


## Take the inpute from user

print("Select Operations.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
choice=input("Enter choice 1/2/3/4/5:")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if choice=='1':
    print(num1, "+", num2,"=", add(num1,num2))

elif choice=='2':
    print(num1, "-", num2, "=", substract(num1, num2))

elif choice=='3':
    print(num1, "x", num2, "=", multiple(num1, num2))

elif choice=='4':
    print(num1, "/", num2, "=", devide(num1, num2))

elif choice=='5':
    print(num1, "*", num2, "=", power(num1, num2))

else:
    print("Invalid input")