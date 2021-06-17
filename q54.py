'''
COIN CHANGE DP-7

Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: 
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
So the output should be 5.

1) Optimal Substructure
To count the total number of solutions, we can divide all set solutions into two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.
Let count(S[], m, n) be the function to count the number of solutions, then it can be written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

Therefore, the problem has optimal substructure property as the problem can be solved using solutions to subproblems.

2) Overlapping Subproblems
Following is a simple recursive implementation of the Coin Change problem. 
The implementation simply follows the recursive structure mentioned above.


'''
# recursive python3 program for coin change probleam
# returns the count of ways we can sum
# s[0.....m-1] coins to get sum n
# def count(s,m,n):

#     # if n is 0 then there is 1
#     # solution (do not include any coin)
#     if (n==0):
#         return 1
    
#     # if n is less than 0 then no
#     # solution exists
#     if (n<0):
#         return 0

#     # if there are no coins and n
#     # is greater than 0, then no solution exit
#     if (m <= 0 and n >= 1):
#         return 0

#     # count is sum of solutions(i)
#     # including s[m-1] (ii) excluding s[m-1]
#     return count(s,m-1,n) + count(s,m,n-s[m-1])

# # driver program to test above function
# arr = [1,2,3]
# m = len(arr)
# print(count(arr,m,4))

def COUNT(S,M,N):

    if N==0:
        return 1
    
    if N < 0:
        return 0

    if (M <= 0 and N >= 1):
        return 0

    return COUNT(S,M-1,N) + COUNT(S,M,N-S[M-1])

# DRIVER FUNCTION
if __name__ == "__main__":
    ARR = [2, 5, 3, 6]
    M = len(ARR)
    N = 10
    print(COUNT(ARR,M,N))


    