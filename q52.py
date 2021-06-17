'''
CHOCOLATE DISTRIBUTION PROBLEAM

Given an array of n integers where each value represents the number of 
chocolates in a packet. Each packet can have a variable number of chocolates. 
There are m students, the task is to distribute chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with 
maximum chocolates and packet with minimum chocolates given to the 
students is minimum.

Examples:

Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and 
we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum 
difference between maximum and minimum packet 
sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 
Explanation:
The set goes like 3,4,7,9,9 and the output 
is 9-3 = 6

Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 
30, 40, 28, 42, 30, 44, 48, 
43, 50} , m = 7 
Output: Minimum Difference is 10 
Explanation:
We need to pick 7 packets. We pick 40, 41, 
42, 44, 48, 43 and 50 to minimize difference 
between maximum and minimum. 

A simple solution is to generate all subsets of size m of arr[0..n-1]. 
For every subset, find the difference between the maximum and minimum elements in it. 
Finally, return the minimum difference.

An efficient solution is based on the observation that to minimize 
the difference, we must choose consecutive elements from a sorted packet. 
We first sort the array arr[0..n-1], then find the subarray of size m with 
the minimum difference between the last and first elements.

Below image is a dry run of the above approach:


'''
# program to solve chocolate distribution probleam

# arr[0..n-1] represents sizes of packets m is number of students
# returns minimum difference between maximum and minimum values of distribuation

# def findMindiff(arr,n,m):

#     # if there are no chocolates or number of students is 0
#     if (m==0 or n==0):
#         return 0

#     # sort the given packats
#     arr.sort()

#     # number of students cannot be more than number of packets
#     if (n<m):
#         return -1

#     min_diff = arr[n-1] - arr[0]

#     # find the subarray of size m such that 
#     # difference between last (maximum in case of sorted)
#     # and first (minimum in case of sorted) elements of subarray is minimum
#     for i in range(len(arr) - m + 1):
#         min_diff = min(min_diff, arr[i+m-1] - arr[i])

#     return min_diff

# # driver code
# if __name__ == '__main__':
#     arr = [12, 4, 7, 9, 2, 23, 25, 41,
#           30, 40, 28, 42, 30, 44, 48, 
#           43, 50]
#     m = 7
#     n = len(arr)
#     print("minimum difference is ",findMindiff(arr,n,m))

def CHOCOLATE(ARR,N,M):

    if (N==0 or M==0):
        return 0

    if (N<M):
        return -1

    ARR.sort()

    MIN_DIFF = ARR[N-1] - ARR[0]
    for I in range(N - M + 1):
        MIN_DIFF = min(MIN_DIFF, ARR[I+M-1] - ARR[I])

    return MIN_DIFF

# DRIVER MODE
if __name__ == '__main__':
    ARR = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    N = len(ARR)
    M = 7
    print(CHOCOLATE(ARR,N,M))
 

