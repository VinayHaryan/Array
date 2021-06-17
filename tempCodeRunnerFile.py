# python arrays
'''
An array is a collection of items stored at contiguous memory locations. The
idea is to store multiple items of the same type together. This makes it
easier to calculate the position of each element by simply adding an offset
to a base value, i.e., the memory location of the first element of the array
(generally denoted by the name of the array).

For simplicity, we can think of an array a fleet of stairs where on each step
is placed a value (let’s say one of your friends). Here, you can identify the
location of any of your friends by simply knowing the count of the step they
are on. Array can be handled in Python by a module named array. They can
be useful when we have to manipulate only a specific data type values. A
user can treat lists as arrays. However, user cannot constraint the type of
elements stored in a list. If you create arrays using the array module, all
elements of the array must be of the same type.

'''
# Creating a Array
# Array in Python can be created by importing array module. array(data_type,
# value_list) is used to create an array with data type and value list specified
# in its arguments.

# python program to demonstrate
# creation of array

# import "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1,2,3])
print(a)

# printing original array 
print("the new created array  is: ", end=" ")
for i in range(0,3):
    print(a[i], end="")

# creating an array with float type
b = arr.array('d',[2.5, 3.2, 3.3])

# printing original array
print("the new created array is : ", end=" ")
for i in range(0,3):
    print(b[i], end=" ")

# Some of the data types are mentioned below which will help in creating an
# array of different data types.
"""
type code , C type , Python type ,Minimum size in Bytes

b, signed cahar, int, 1
B, unsigned char, int, 1
u, Py_UNICODE, unicode charcter, 2
h, signed short, int, 2
H, usigned short int, 2
i, signed int, int, 2
I, unsigned int, int, 2
l, signed long, int, 4
L, unsigned long, int, 4
'q' signed long long, int, 8
Q unsigned long long, int, 8
f, float, 4
d, double, float, 8

"""
# Adding Elements to a Array
'''
Elements can be added to the Array by using built-in insert() function.
Insert is used to insert one or more data elements into an array. Based on
the requirement, a new element can be added at the beginning, end, or any
given index of array. append() is also used to add the value mentioned in its
arguments at the end of the array.

'''
# python program to demonstrate
# adding elements to a array
# importing array for array creations

import array as arr
# array with int type
a = arr.array('i',[1,2,3])

print("array before insertion: ", end=" ")
for i in range(0,3):
    print(a[i], end=" ")

# inserting array using
# insert() function
a.insert(1,4)
print('\n')
for i in (a):
    print(i, end=" ")

# array with float type
print("\n")
b = arr.array('d', [2.5, 3.2, 3.3])
for i in range(0, 3):
    print(b[i], end=' ')

print("\n")
b.append(4.4)
for i in (b):
    print(i, end=" ")

# Accessing elements from the array
# In order to access the array items refer to the index number. Use the index
# operator [ ] to access an item in a array. The index must be an integer.

# python program to demonstrate
# accessing of element from list
import array as arr
# array with int type
a = arr.array('i',[1,2,3,4,5,6])

print('\n')
# accessing element of array
print("Acess elements is: ", a[0])

# accessing element of array
print("Acess elements is: ",a[3])

# array with float type
b = arr.array('d',[2.5, 3.5, 3.3])

# accessing element of array
print("acess element is: ",b[1])

# accessing element of array
print("access element is: ",b[2])

# Removing elements from the array
# Elements can be removed from the array by using built-in remove() function
# but an Error arises if element doesn’t exist in the set. Remove() method only
# removes one element at a time, to remove range of elements, iterator is
# used. pop() function can also be used to remove and return an element from
# the array, but by default it removes only the last element of the array, to
# remove element from a specific position of the array, index of the element is
# passed as an argument to the pop() method.
# Note – Remove method in List will only remove the first occurrence of the
# searched element

# Removal of elements in a array
print("\n")
import array
arr = array.array('i',[1,2,3,1,5])
# printing original array
print("the new created array is: ", end="")
for i in range(0,5):
    print(arr[i], end=" ")

print('\r')

# using pop() to remove element at 2nd position
print("the popped element is: ", end="")
print(arr.pop(2))
print("after poping")
for i in (arr):
    print(arr, end=" ")