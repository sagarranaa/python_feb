from array import *

# arr=array('i',[5,7,8,9,7,5])
# print(arr.buffer_info())
# arr.reverse()
#How to create new array with the same vale
# New_array=array(arr.typecode,(a*a for a in arr))
# for i in range(len(New_array)):
#     print(arr[i])
#1. write a code to sort the array in ascending order
# Initialize array
arr = [5, 2, 8, 7, 1];
temp = 0;

# Displaying elements of original array
print("Elements of original array: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");

# Sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

print();

# Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ");
for i in range(0, len(arr)):
    print(arr[i], end=" ");