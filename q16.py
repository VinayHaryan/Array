'''
Program to cyclically rotate an array by one

Given an array, cyclically rotate the array clockwise by one

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}

Following are steps 
1) store last elements in a variable say x
2) shift all elements one position ahead
3) Replace first element of array with x

'''
# code for program to cyclically roatate an array by one
# method for rotation

# def rotate(arr, n):
#     x =arr[n-1]

#     for i in range(n - 1, 0, -1):
#         arr[i] = arr[i - 1]

#     arr[0] = x

# # driver function
# arr = [1,2,3,4,5]
# n = len(arr)
# print("given array is")
# for i in range(0,n):
#     print(arr[i],end=' ')

# rotate(arr, n)
# print('\nRotate array is')
# for i in range(0,n):
#     print(arr[i], end=' ')


def rotate(arr, n):
    x = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = x

# diriver function
arr=[1,2,3,4,5,6,7,8,9]
n = len(arr)

print('\ngiven array')
for i in range(n):
    print(arr[i], end=' ')

rotate(arr,n)

print("\nrotate array")
for i in range(n):
    print(arr[i], end=' ')



