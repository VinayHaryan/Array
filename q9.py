'''
Sort an array of 0s, 1s and 2s

Given an array A[] consisting 0s, 1s, and 2s. the task is
to write a function that sorts the given array. the functions 
should put all 0s first, them all 1s and all 2s in last

Examples:

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

'''
# python program to sort an array with 0,1 and 2 in a single pass
# function to sort array

# def sort012(a, arr_size): 
#     lo = 0
#     hi = arr_size - 1
#     mid = 0
#     while mid <= hi: 
#         if a[mid] == 0: 
#             a[lo], a[mid] = a[mid], a[lo] 
#             lo = lo + 1
#             mid = mid + 1
#         elif a[mid] == 1: 
#             mid = mid + 1
#         else: 
#             a[mid], a[hi] = a[hi], a[mid]  
#             hi = hi - 1
#     return a 
      
# # Function to print array 
# def printArray( a): 
#     for k in a: 
#         print(k, end=' ') 
    
# # Driver Program 
# a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
# arr_size = len(a) 
# arr = sort012(a, arr_size) 
# printArray(arr)

def sort_012(arr, arr_size):
    lo = 0
    hi = arr_size - 1
    med = 0
    while med <= hi:
        if arr[med] == 0:
            arr[lo], arr[med] = arr[med], arr[lo]
            lo = lo + 1
            med = med + 1

        elif arr[med] == 1:
            med = med + 1

        else:
            arr[med], arr[hi] = arr[hi], arr[med]
            hi = hi - 1

    return arr

def printing(arr):
    for i in arr:
        print(i, end=' ')


arr = [0,0,1,1,0,0,2,2,0]
arr_size = len(arr)
arrr = sort_012(arr,arr_size)
printing(arrr)

# Time Complexity O(n)
# only one traversal of the array is needed
# space Complexity O(1)
# NO extra space is required

# the above code performs unnecessary for some inputs
# which are not really required. it can be modified to
# reduce some swaps 

#


