'''

GIVEN A SORTED ARRAY AND A NUMBER X,
FIND PAIR IN ARRAY WHOSE SUM IS CLOSET TO X

Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

A simple solution is to consider every pair and keep track of closest pair 
(absolute difference between pair sum and x is minimum). 
Finally, print the closest pair. Time complexity of this solution is O(n2)

An efficient solution can find the pair in O(n) time. The idea is similar to method 1 of this post. 
The following is a detailed algorithm. 

1) Initialize a variable diff as infinite (Diff is used to store the 
   difference between pair and x).  We need to find the minimum diff.
2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index:  l = 0
       (b) Initialize second  the rightmost index:  r = n-1
3) Loop while l < r.
       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
           update diff and result 
       (b) If(arr[l] + arr[r] <  sum )  then l++
       (c) Else r--    

'''
# program to find the pair with sum
# closet to agiven no
# a sufficiently large value grater than any
# element in the input array

# max_val = 10000

# # print the pair with sum closet to x
# def printcloset(arr,n,x):
    
#     # to store indexes of result pair
#     res_l, res_r = 0,0

#     # initialize left and right indexes
#     # and difference between pair sum and x
#     l, r, diff = 0, n-1, max_val
#     while r>l:
#         # check if this pair is closer than the 
#         # closet pair so far
#         if abs(arr[l] + arr[r]-x) < diff:
#             res_l = l
#             res_r = r
#             diff = abs(arr[l] + arr[r] - x)

#         if arr[l] + arr[r] > x:
#             # if this pair has more sum, move to
#             # smaller values
#             r -= 1
#         else:
#             # move to larger values
#             l += 1

#     print('the closet pair is {} and {}'.format(arr[res_l],arr[res_r]))


# # Driver code to test above
# if __name__ == "__main__":
#     arr = [10,22,28,29,30,40]
#     n = len(arr)
#     x = 54
#     printcloset(arr,n,x)

MAX_VAL = 1000
def PRINTCLOSET(ARR,N,X):
    RES_R, RES_L =0,0
    L,R,DIFF = 0,N-1,MAX_VAL

    while (R>L):
        if abs(ARR[L] + ARR[R] - X ) < DIFF:
            RES_L = L
            RES_R = R
            DIFF = abs(ARR[L] + ARR[R] - X) 

        if ARR[L] + ARR[R] > X:
            R -= 1
        else:
            L += 1

    print("CLOSET ",ARR[RES_L],ARR[RES_R])

# DRIVER FUNCTION
if __name__ == '__main__':
    ARR = [10,22,28,29,30,40]
    N = len(ARR)
    X = 54
    PRINTCLOSET(ARR,N,X)
