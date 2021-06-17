'''
Find if there is a subarray with 0 sum

Given an array of positive and negative numbers, find if there is a 
subarray (of size at least one) with 0 sum

Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 2 to 2.

Input: {-3, 2, 3, 1, 6}
Output: false

a simple solution is to consider all subarrays one by one and check the sum
of every subarray. we can run two loops: the outer loop picks a starting
point i and the inner loop tries all subarrays starting from i. the time complexity
of this method is O(n2) 

we can use hashing. the idea is to iterate through the array and for every element arr[i],
calculate the sum of elements from 0 to i (this can simply done as sum += arr[i]). if the 
current sum has been seen before, then there is a zero-sum array. hashing is used to store the 
sum values so that we can quickly store sum and find out whether the current sum is seen before or not


Example :

arr[] = {1, 4, -2, -2, 5, -4, 3}
If we consider all prefix sums, we can
notice that there is a subarray with 0
sum when :
1) Either a prefix sum repeats or
2) Or prefix sum becomes 0.

Prefix sums for above array are:
1, 5, 3, 1, 6, 2, 5

Since prefix sum 1 repeats, we have a subarray
with 0 sum. 

'''
# # program to fine if there is a zero sum subarray
# def subarrayExists(arr,n):
#     # traverse through array
#     # and store prefix sums
#     n_sum = 0
#     s = set()

#     for i in range(n):
#         n_sum += arr[i]

#         # if prefix sum is 0 or 
#         # it is already present
#         if n_sum == 0 or n_sum in s:
#             return True
#         s.add(n_sum)
#     return False

# # driver code
# arr = [-3, 2, 3, 1, 6]
# n = len(arr)
# if subarrayExists(arr,n) == True:
#     print("found a subarray with o sum")
# else:
#     print("no such sub array exits!")

def SUBARRAY_EXISTS(ARR,N):
    N_SUM = 0
    S = set()
    for I in range(N):
        N_SUM += ARR[I]
        if N_SUM == 0 or N_SUM in S:
            return True
        S.add(N_SUM)

    return False

# DRIVER FUNCTION
ARR = [1,4,-2,-2,5,-4,3]
N = len(ARR)
if SUBARRAY_EXISTS(ARR,N) == True:
    print('ZERO SUM PRESENT THERE')
else:
    print("NO ZERO SUM SUBARRAY")


'''
Time complexity of this solution can be consider as O(n) under the
assumption that we have good hashing function that allows insertion and
retrieval operations in O(1) time

space complexity O(n) here we requred extra space for unordered_set to insert
array elements



'''