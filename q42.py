'''
FIND WHWTHER AN ARRAY IS SUBSET OF ANOTHER ARRAY 

Given two arrays: arr1[0..m-1] and arr2[0..n-1]. 
Find whether arr2[] is a subset of arr1[] or not. 
Both the arrays are not in sorted order. 
It may be assumed that elements in both array are distinct.

Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
Output: arr2[] is not a subset of arr1[] 

'''

# program to find whether an array
# is subset of another array
# return true if arr2[] is subset of arr1[]

# def isSubset(arr1, m, arr2, n):
#     # create a frequency table using STL

#     frequency = {}

#     # increase the frequency of each element
#     # in the frequency table
#     for i in range(0, m):
#         if arr1[i] in frequency:
#             frequency[arr1[i]] = frequency[arr1[i]] + 1
#         else:
#             frequency[arr1[i]] = 1

    
#     # decrease the frequency is the 
#     # element was found in the frequency
#     # table with the frequency more than 0
#     # else return 0 and if loop is
#     # completed return 1

#     for i in range(0, n):
#         if (frequency[arr2[i]] > 0):
#             frequency[arr2[i]] -= 1
#         else:
#             return False
#     return True

# # driver code
# if __name__ == '__main__':
#     arr1 = [ 11, 1, 13, 21, 3, 7 ]
#     arr2 = [ 11, 3, 7, 1 ]
     
#     m = len(arr1)
#     n = len(arr2)

#     if (isSubset(arr1,m,arr2,n)):
#         print("arr2[] is subset of arr1[] ")
#     else:
#         print("arr2[] is not a subset of arr1[] ")



def ISSUBARRAY(ARR1,M,ARR2,N):
    FREQUNCY = {}
    for I in range(0,M):
        if ARR1[I] in FREQUNCY:
            FREQUNCY[ARR1[I]] = FREQUNCY[ARR1[I]] + 1
        else:
            FREQUNCY[ARR1[I]] = 1

    for I in range(0,N):
        if (FREQUNCY[ARR2[I]] > 0):
            FREQUNCY[ARR2[I]] -= 1
        else:
            return False
    return True

# DRIVER CODE
if __name__ == '__main__':
    ARR1 = [1,2,3,4,5,6]
    ARR2 = [1,2,4]

    M = len(ARR1)
    N = len(ARR2)

    if (ISSUBARRAY(ARR1,M,ARR2,N)):
        print("ARR2[] IS SUBARRAY OF ARR1[]")

    else:
        print("ARR2[] IS NOT SUBARRAY OF ARR1[]")
        
'''
TIME COMPLEXITY
O(M+N)

'''






