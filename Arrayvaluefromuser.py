from array import *
# arr=array('i',[])
# n=int(input("Enter the length of Array:"))
# for i in range(n):
#     x=int(input("Enter the value in array:"))
#     arr.append(x)
# print(arr)
# val=int(input("Enter the value of search?"))
# k=0 #counter variable
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k=k+1
#Assignments Questions
##1.create an array with 5 value and delete the value at index 2 number without using in-built function.
#2.Write a code to reverse an array without using in-built function

# arr=array('i',[5,7,8,9,8])
# arr=[2,4,7,8,9]
# z=[]
# for i in range(len(arr)):
#     if i==2:
#         continue
#         z.append(i)
#     else:
#         print(arr[i],end=" ")

ar=array('i',[7,8,9,7,8])
# ar.reverse()
inver=array(ar.typecode,[])
for i in range(len(ar)):
    inver.append((ar[len(ar)-i-1]))
print(inver)