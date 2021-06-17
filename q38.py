'''
FIND A TRIPLET THAT SUM TO A GIVEN VALUE


Given an array and a value, 
find if there is a triplet in array whose sum is equal to the given value. 
If there is such a triplet present in array, 
then print the triplet and return true. Else return false. 

Example: 

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
Output: 12, 3, 9
Explanation: There is a triplet (12, 3 and 9) present
in the array whose sum is 24. 

Input: array = {1, 2, 3, 4, 5}, sum = 9
Output: 5, 3, 1
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9. 

'''
# program to find a triplet using Hashing
# returns true if there is triplet with sum equal
# to sum present in a[]. also, prints the triplet

# def find3numbers(a, arr_size, sum):
#     for i in range(0,arr_size-1):
#         # find pair in subarray a[i+1...n-1]
#         # with sum equal to sum - a[i]
#         s = set()
#         curr_sum = sum - a[i]
#         for j in range(i+1, arr_size):
#             if (curr_sum - a[j]) in s:
#                 print("triplet is",a[i],", ",a[j],', ',curr_sum-a[j])
#                 return True
#             s.add(a[j])
#     return False

# # Driver program to test above function
# a = [1,4,45,6,10,8]
# sum = 22
# arr_size = len(a)
# find3numbers(a, arr_size, sum)


def FIND3NUMBERSSUM(ARR,ARR_SIZE,SUM):
    for I in range(0,ARR_SIZE-1):
        # FIND PAIR IN SUBARRAY WITH SUM EQUAL
        S = set()
        CURR_SUM = SUM - ARR[I]
        for J in range(I+1,ARR_SIZE):
            if (CURR_SUM - ARR[J]) in S:
                print("TRIPLET OF GIVEN SUM IS - ",ARR[I],ARR[J],CURR_SUM-ARR[J])
                return True

            S.add(ARR[J])

    return False

# DRIVER PROGRAM TO TEST ABOVE FUNCTION
A = [1,4,45,6,10,8]
SUM = 22
ARR_SIZE = len(A)
FIND3NUMBERSSUM(A,ARR_SIZE,SUM)

'''
Complexity Analysis: 
Time complexity: O(N^2). 
There are only two nested loops traversing the array, so time complexity is O(n^2).
Space Complexity: O(N). 
As no extra space is required. 

'''