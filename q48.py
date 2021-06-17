'''
MAXIMUM SUM PATH IN TWO ARRAYS

Given two sorted arrays, such that the arrays may have some 
common elements. Find the sum of the maximum sum path to reach 
from the beginning of any array to end of any of the two arrays. 
We can switch from one array to another array only at common elements. 

Note: The common elements do not have to be at the same indexes.


Input: ar1[] = {2, 3, 7, 10, 12}
       ar2[] = {1, 5, 7, 8}
Output: 35

Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12.
We start from the first element of arr2 which is 1, then we
move to 5, then 7.  From 7, we switch to ar1 (as 7 is common)
and traverse 10 and 12.

Input: ar1[] = {10, 12}
       ar2 = {5, 7, 9}
Output: 22

Explanation: 22 is the sum of 10 and 12.
Since there is no common element, we need to take all 
elements from the array with more sum.

Input: ar1[] = {2, 3, 7, 10, 12, 15, 30, 34}
        ar2[] = {1, 5, 7, 8, 10, 15, 16, 19}
Output: 122

Explanation: 122 is sum of 1, 5, 7, 8, 10, 12, 15, 30, 34


Note: The common elements do not have to be at the same indexes.
Expected Time Complexity: O(m+n), 
where m is the number of elements in ar1[] and n is the number of elements in ar2[].

Efficient Approach: The idea is to do something similar to merge process of
merge sort. This involves calculating the sum of elements between all common 
points of both arrays. Whenever there is a common point, compare the two sums 
and add the maximum of two to the result.

Algorithm: 

1.Create some variables, result, sum1, sum2. 
Initialize result as 0. 
Also initialize two variables sum1 and sum2 as 0. 
Here sum1 and sum2 are used to store sum of element in ar1[] and ar2[] respectively. 
These sums are between two common points.

2.Now run a loop to traverse elements of both arrays. 
While traversing compare current elements of array 1 and array 2 
in the following order.

2.1 If current element of array 1 is smaller than current element of 
array 2, then update sum1, else if current element of array 2 is 
smaller, then update sum2.

2.2 If the current element of array 1 and array 2are same, 
then take the maximum of sum1 and sum2 and add it to the result. 
Also add the common element to the result.

2.3 This step can be compared to the merging of two sorted arrays, 
If the smallest element of the two current array indices is processed 
then it is guaranteed that if there is any common element it will be 
processed together.So the sum of elements between two common elements 
can be processed.


'''

# Python program to find maximum sum path
 
# This function returns the sum of elements on maximum path from
# beginning to end
 
 
# def maxPathSum(ar1, ar2, m, n):
 
#     # initialize indexes for ar1[] and ar2[]
#     i, j = 0, 0
 
#     # Initialize result and current sum through ar1[] and ar2[]
#     result, sum1, sum2 = 0, 0, 0
 
#     # Below 3 loops are similar to merge in merge sort
#     while (i < m and j < n):
 
#         # Add elements of ar1[] to sum1
#         if ar1[i] < ar2[j]:
#             sum1 += ar1[i]
#             i += 1
 
#         # Add elements of ar2[] to sum2
#         elif ar1[i] > ar2[j]:
#             sum2 += ar2[j]
#             j += 1
 
#         else:   # we reached a common point
 
#             # Take the maximum of two sums and add to result
#             result += max(sum1, sum2)
 
#             # Update sum1 and sum2 for elements after this intersection point
#             sum1, sum2 = 0, 0
 
#             # Keep updating result while there are more common elements
#             temp = i
#             while i < m and ar1[i] == ar2[j]:
#                 sum1 += ar1[i];
#                 i += 1
#             while j<n and ar1[temp] == ar2[j]:
#                 sum2 += ar2[j]
#                 j += 1
#             result += max(sum1,sum2)
#             sum1 = sum2 = 0;           
 
#     # Add remaining elements of ar1[]
#     while i < m:
#         sum1 += ar1[i]
#         i += 1
#     # Add remaining elements of b[]
#     while j < n:
#         sum2 += ar2[j]
#         j += 1
 
#     # Add maximum of two sums of remaining elements
#     result += max(sum1, sum2)
 
#     return result
 
 
# # Driver code
# ar1 = [2, 3, 7, 10, 12, 15, 30, 34]
# ar2 = [1, 5, 7, 8, 10, 15, 16, 19]
# m = len(ar1)
# n = len(ar2)
 
# # Function call
# print ("Maximum sum path is", maxPathSum(ar1, ar2, m, n))


def MAXSUMPATH(ARR1, ARR2, M, N):
    I,J = 0,0
    SUM1, SUM2, RESULT = 0,0,0
    while (I<M and J<N):
        if ARR1[I] < ARR2[J]:
            SUM1 += ARR1[I]
            I += 1

        elif ARR1[I] > ARR2[J]:
            SUM2 += ARR2[J]
            J += 1

        else:
            RESULT += max(SUM1,SUM2)
            SUM1, SUM2 = 0,0

            TEMP = I
            while I<M and ARR1[I] == ARR2[J]:
                SUM1 += ARR1[I]
                I += 1

            while J<N and ARR1[TEMP] == ARR2[J]:
                SUM2 += ARR2[J]
                J += 1
            
            RESULT += max(SUM2,SUM1)
            SUM1, SUM2 = 0,0

    while I < M:
        SUM1 += ARR1[I]
        I += 1

    while J < N:
        SUM2 += ARR2[J]
        J += 1

    RESULT += max(SUM2,SUM1)
    
    return RESULT

# DRIVER MODE 
ARR1 = [2, 3, 7, 10, 12, 15, 30, 34]
ARR2 = [1, 5, 7, 8, 10, 15, 16, 19]
M = len(ARR1)
N = len(ARR2)

print("MAX PATH SUM IS: ",MAXSUMPATH(ARR1,ARR2,M,N))


'''
Complexity Analysis:  

Space Complexity: O(1). 
Any extra space is not required, so the space complexity is constant.

Time complexity: O(m+n). 
In every iteration of while loops, an element from either of the two arrays 
is processed. There are total m + n elements. Therefore, the time complexity is O(m+n).

'''




            

    
