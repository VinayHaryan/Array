'''
PRINT A GIVEN MATRIX IN SPIRAL FORM

Given 2D array, print it in spiral form. see the following examples

Examples: 

Input:  1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

Input:  1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
Explanation :The output is matrix in spiral format.


Method 3: (Recursive Approach)

Approach: The above problem can be solved by printing the boundary of the Matrix recursively. 
In each recursive call, we decrease the dimensions of the matrix. 
The idea of printing the boundary or loops is the same.

Algorithm: 
1.create a recursive function that takes a matrix and some variables 
(k – starting row index, m – ending row index, l – starting column index, n – ending column index) 
as parameters
2.Check the base cases (stating index is less than or equal to ending index) and print the 
boundary elements in clockwise manner
3.Print the top row, i.e. Print the elements of kth row from column index l to n, and increase the count of k.
4.Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of n.
5.Print the bottom row, i.e. if k > m, then print the elements of m-1th row from column n-1 to l and decrease the count of m
6.Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to k and increase the count of l.
7.Call the function recursively with the values of starting and ending indices of rows and columns.

'''
# program for the above approch
# function for printing matrix, row
# and column respectively m,n: end index
# of matrix row and column respectively
# def printdata(arr,i,j,m,n):

#     # if i or j lies ouside tha matrix
#     if (i >= m or j >=n):
#         return

#     # print first row
#     for p in range(i,n):
#         print(arr[i][p], end=' ')

#     # print last column
#     for p in range(i+1, m):
#         print(arr[p][n - 1], end=' ')

#     # print last row, if last and first row not same
#     if ((m-1) != i):
#         for p in range(n-2, j-1,-1):
#             print(arr[m-1][p], end=' ')

#     # print first column, if last and first column are not same
#     if ((n-1) != j):
#         for p in range(m-2,i,-1):
#             print(arr[p][j], end=' ')

#     printdata(arr,i+1,j+1,m-1, n-1)


# # driver code 
# R = 4
# C = 4
# arr = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
 

# printdata(arr, 0, 0, R, C)


# # Python3 program to print
# # given matrix in spiral form
 
 
# def spiralPrint(m, n, a):
#     k = 0
#     l = 0
 
#     ''' k - starting row index
#         m - ending row index
#         l - starting column index
#         n - ending column index
#         i - iterator '''
 
#     while (k < m and l < n):
 
#         # Print the first row from
#         # the remaining rows
#         for i in range(l, n):
#             print(a[k][i], end=" ")
 
#         k += 1
 
#         # Print the last column from
#         # the remaining columns
#         for i in range(k, m):
#             print(a[i][n - 1], end=" ")
 
#         n -= 1
 
#         # Print the last row from
#         # the remaining rows
#         if (k < m):
 
#             for i in range(n - 1, (l - 1), -1):
#                 print(a[m - 1][i], end=" ")
 
#             m -= 1
 
#         # Print the first column from
#         # the remaining columns
#         if (l < n):
#             for i in range(m - 1, k - 1, -1):
#                 print(a[i][l], end=" ")
 
#             l += 1
 
 
# # Driver Code
# a = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
 
# R = 4
# C = 4
 
# # Function Call
# spiralPrint(R, C, a)
 

def SPIRALPRINT(M,N,A):
    K = 0
    L = 0
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
    while (K < M and L < N):
        
        for I in range(L,N):
            print(A[K][I], end=' ')
        K += 1

        for I in range(K,M):
            print(A[I][N-1], end=' ')
        N -= 1

        if (K < M):
            for I in range(N-1,(L-1),-1):
                print(A[M-1][I],end=" ")
            M -= 1

        if (L < N):
            for I in range(M-1,K-1,-1):
                print(A[I][L], end=' ')
            L += 1

# DRIVER MODE
A = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]

C = 6
R = 3

SPIRALPRINT(R,C,A)
