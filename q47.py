'''
GIVEN AN ARRAY ARR[], FIND THE MAXIMUM J-I SUCH 
THAT ARR[J] > ARR[I]

https://www.youtube.com/watch?v=70WKqk3FU08

Examples : 

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1 

'''

# utility function to get max
# and minimum of two integers
def max(a,b):
    if (a>b):
        return a
    else:
        return b

def min(a,b):
    if (a<b):
        return a
    else:
        return b

# for a given array[],
# returns the maximum j-i
# such that arr[j] > arr[i]
# def maxIndexDiff(arr,n):
    
#     lmin = [0]*n
#     rmax = [0] *n

#     # construct lmin[] such that
#     # lmin[i] stores the minimum
#     # value from (arr[0], arr[1], .....arr[i])
#     lmin[0] = arr[0]
#     for i in range(1,n):
#         lmin[i] = min(arr[i], lmin[i-1])

#     # construct rmax[] such that
#     # rmax[j] stores the maximum
#     # value from (arr[j], arr[j+1],...arr[n-1])
#     rmax[n-1] = arr[n-1]
#     for j in range(n-2,-1,-1):
#         rmax[j] = max(arr[j], rmax[j+1])

#     i, j = 0,0
#     maxdiff = -1
#     while (j<n and i<n):
#         if (lmin[i] < rmax[j]):
#             maxdiff = max(maxdiff, j-i)
#             j = j+1
#         else:
#             i = i + 1

#     return maxdiff

# # driver code
# if __name__ == '__main__':
#     arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
#     n = len(arr)
#     maxdiff = maxIndexDiff(arr,n)
#     print(maxdiff)



def MAXINDEXDIFF(ARR,N):
    LMIN = [0] * N
    RMAX = [0] * N

    # FILL LMIN
    LMIN[0] = ARR[0]
    for I in range(1,N):
        LMIN[I] = min(LMIN[I-1], ARR[I])

    # FILL RMAX
    RMAX[N-1] = ARR[N-1]
    for J in range(N-2,-1,-1):
        RMAX[J] = max(RMAX[J+1], ARR[J])

    I,J=0,0
    MAXDIFF = -1
    while J<N and I<N:
        if LMIN[I] < RMAX[J]:
            MAXDIFF = max(MAXDIFF,J-I)
            J = J+1
        else:
            I = I + 1

    return MAXDIFF

# DRIVER FUNCTION
if __name__ == "__main__":
    ARR = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    N = len(ARR)
    print("MAXDIFF= ",MAXINDEXDIFF(ARR,N))

    

