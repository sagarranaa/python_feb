# wrtite a code which is divisible by 3 and 5 & skip all those no
#continue statement
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         continue
#     print(i,end=" ")
# print("Byye")

# Using while loop
# i=101
# while i>=101:
#     if i%3==0 or i%5==0:
#         continue
#
#     print(i,end=" ")
#     i=i-1
#Question of the Day
# 1.Print first 50 fibonacci series number
#2. Check a given number is prime or not
first=0
second=1
num=int(input("Enter number of digit ,which you want!"))
print("\nfibbonacci series is.")
print(first,",",second,end=",")
for i in range(2,num):

    next=first+second
    print(next,end=",")
    first=second
    second=next



