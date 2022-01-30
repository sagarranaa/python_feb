import sys # by sys function we can increase the limit of recusion function
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())

def recur():
    print("Hello World")
    recur()
recur()
