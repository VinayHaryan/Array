'''
FIND THE ROW WITH MAXIMUM NUMBER OF 1S

given a boolean 2D array, where each row is sorted.
find the row with the maximum number of 1s

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2


A simple method is to do a row wise traversal of the matrix, 
count the number of 1s in each row and compare the count with max. 
Finally, return the index of row with maximum 1s. 
The time complexity of this method is O(m*n) where m is number of rows 
and n is number of columns in matrix.

We can do better. Since each row is sorted, we can use Binary Search to count of 1s 
in each row. We find the index of first instance of 1 in each row. The count of 1s 
will be equal to total number of columns minus the index of first 1.
See the following code for implementation of the above approach. 

'''

# program to find the row 
# with maximum number of 1s
# function to find the index 
# of first index of 1 in a
# boolean array arr[]

# def first(arr, low, high):
#     if high >= low:
#         # get the middle index
#         mid = low + (high - low) // 2

#         # check if the element at 
#         # middle index is first 1
#         if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#             return mid

#         # if the element is 0
#         # recur for right side
#         elif arr[mid] == 0:
#             return first(arr, (mid + 1), high)

#         # if element is not first 1
#         # recur for left side
#         else:
#             return first(arr,low,(mid - 1))

#     return -1

# # functin that returns 
# # index of row with maximum
# # number of 1s
# def rowwithmaxis(mat):

#     # initialize max values
#     R = len(mat)
#     c = len(mat[0])
#     max_row_index = 0
#     max = -1

#     # traverse for each row and 
#     # count number of 1s by finding
#     # the index of first 1
#     for i in range(0,R):
#         index = first(mat[i], 0, c - 1)
#         if index != -1 and c - index > max:
#             max = c - index
#             max_row_index = i
#     return max_row_index

# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# print ("Index of row with maximum 1s is", 
#       rowwithmaxis(mat))




def FIRST(ARR,LOW,HIGH):
    if HIGH >= LOW:
        MID = LOW + (HIGH - LOW) // 2
        if (MID == 0 or ARR[MID-1] == 0) and ARR[MID] == 1:
            return MID

        elif(ARR[MID] == 0):
            return FIRST(ARR,(MID+1),HIGH)

        else:
            return FIRST(ARR,LOW,(MID-1))

    return -1

def MATRIXWITTHMAX1S(MAT):
    R = len(MAT)
    C = len(MAT[0])
    MAX = -1
    MAX_ROW_INDEX = 0
    for I in range(0,R):
        INDEX = FIRST(MAT[I],0,C-1)
        if INDEX != -1 and C - INDEX > MAX:
            MAX = C - INDEX
            MAX_ROW_INDEX = I
    return MAX_ROW_INDEX

# DRIVER CODE
MAT = [[0, 0, 0, 1],
       [1, 1, 1, 1],
       [0, 1, 1, 1],
       [0, 0, 0, 0]]


print("INDEX OF ROW WITH MAXIMUM 1S IS", MATRIXWITTHMAX1S(MAT))

'''
TIME COMPLEXITY O(MLOGN) WHERE M IS NUMBER OF ROWS AND N IS NUMBER OF COLUMNS IN MATRIX

'''

