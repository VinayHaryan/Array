'''
FIND THE REPEATING AND THE MISSING ADDED 3 NEW METHOD

Given an unsorted array of size n. Array elements are in the range 
from 1 to n. One number from set {1, 2, …n} is missing and one number 
occurs twice in the array. Find these two numbers.

Examples: 

Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 
2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1

Make two equations using sum and sum of squares
Approach:
Let x be the missing and y be the repeating element.

Let N is the size of array.

Get the sum of all numbers using formula S = N(N+1)/2

Get the sum of square of all numbers using formula Sum_Sq = N(N+1)(2N+1)/6

Iterate through a loop from i=1….N

S -= A[i]

Sum_Sq -= (A[i]*A[i])

It will give two equations 

x-y = S – (1) 

x^2 – y^2 = Sum_sq 

x+ y = (Sum_sq/S) – (2) 



'''
# def repeatedNumber(a):

#     length = len(a)
#     sum_n = (length*(length+1))//2
#     sum_nsq = ((length * (length+1)* (2 * length + 1))//6)

#     missingNumber, repeating = 0,0
#     for i in range(len(a)):
#         sum_n -= a[i]
#         sum_nsq -= a[i] * a[i]
    
#     missingNumber = (sum_n + sum_nsq//sum_n)//2

#     repeating = missingNumber - sum_n

#     ans = []
#     ans.append(repeating)
#     ans.append(missingNumber)
#     return ans

# # driver code
# v = [4, 3, 6, 2, 1, 6, 7]
# res = repeatedNumber(v)
# for i in res:
#     print(i, end=' ')

def MISSINGREPEATING(ARR):
    LENGTH = len(ARR)
    SUM_N = (LENGTH * (LENGTH + 1))//2
    SUM_NSQ = ((LENGTH * (LENGTH +1) * (2 * LENGTH + 1))//6)

    REPEATING , MISSING = 0,0
    for I in range(len(ARR)):
        SUM_N -= ARR[I]
        SUM_NSQ -= ARR[I] * ARR[I]

    MISSING = (SUM_N + SUM_NSQ//SUM_N)//2
    REPEATING = MISSING - SUM_N

    ANS = []
    ANS.append(REPEATING)
    ANS.append(MISSING)

    return ANS


# dRIVETR CODE
v = [ 3,1,3 ]
RES = MISSINGREPEATING(v)
 
for I in RES:
    print(I, end = " ")
