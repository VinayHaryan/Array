'''
CONSTRUCT A UNIQUE MATRIX NXN FOR AN INPUT N

Given an odd integer n, find a matrix of size n x n with following conditions:

Each cell contains an integer from 1 and n (inclusive).
No integer appears twice in the same row or the same column.
All 1’s must be at every possible distance from the center of the matrix. The center of a n x n square is cell ((n-1)/2, (n-1)/2) for odd n.

Example :

Input  : n = 1
Output : 1

Input : n = 3
Output: 3 2 1
        1 3 2
        2 1 3

Input : n = 5
Output : 5 3 2 4 1 
         1 4 3 5 2 
         2 5 4 1 3 
         3 1 5 2 4 
         4 2 1 3 5 

The idea is to first decide positions of 1s. Once possible arrangement of 1s for n = 5 is,

_ _ _ _ 1 
1 _ _ _ _ 
_ _ _ 1 _ 
_ 1 _ _ _ 
_ _ 1 _ _ 


Once we have decided 1s, task of filling remaining items is simple. 
We fill remaining entries column by column. 
For every 1, we traverse its column and fill all entries below it with 
2, 3,…p and fill all entries above it with p+1, .. n. We get following.

5 3 2 4 1 
1 4 3 5 2 
2 5 4 1 3 
3 1 5 2 4 
4 2 1 3 5 

To decide initial positions of 1s, we traverse all rows and keep track of two column numbers “left” and “right”.
1) “right” starts with n-1 and keep decrementing after every alternate row.
2) “left” starts with 0 and keep incrementing after every alternate row.


'''

max = 100
mat = [[0 for x in range(max)] for y in range(max)]

# fills non-one enters in columns j
# given that there is a 1 at position mat[i][j] this function
# position mat[i][j], this function
# fills other entries of column j
def fillRemaining(i,j,n):
        # initialize value to be filled 
        x = 2 
        # fill all values below i as 2, 3, ...p
        for k in range(i+1,n):
                mat[k][j] = x
                x += 1

        # fill all values above i
        # as p+1, p+2, ..n
        for k in range(i):
                mat[k][j] = x
                x += 1

        
# fills entries in mat[][]
# with the given set of rules
def constructMatrix(n):
        # alternatively fill is starting from
        # rightmost and lefmost columns for 
        # example for n=3, we get {_ _ 1}
        right = n - 1
        left = 0
        for i in range(n):

                if (i % 2 == 0):
                        mat[i][right] = 1

                        # after filling 1, fill remaining
                        # entries of column 'right'
                        fillRemaining(i,right,n)

                        # moce right one column back
                        right -= 1

                # fill next column from left
                else:
                        mat[i][left] = 1

                        # after filling 1, fill remaining
                        # entries of column 'left'
                        fillRemaining(i,left,n)

                        # move left one column forward
                        left += 1

# Driver code
n = 5

# passing n to constructMatrix function
constructMatrix(n)

# printing the disired unique matrix
for i in range(n):
        for j in range(n):
                print(mat[i][j], end=' ')
        print("")



        
