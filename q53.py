'''
PRINT ALL POSSIBLE COMBINATIONS OF R ELEMENTS IN A 
GIVEN ARRAY OF SIZE N

Given an array of size n, generate and print all possible combinations 
of r elements in array. For example, if input array is {1, 2, 3, 4} 
and r is 2, then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

Following are two methods to do this.

Method 2 (Include and Exclude every element)
Like the above method, We create a temporary array data[]. 
The idea here is similar to Subset Sum Problem. 
We one by one consider every element of input array, 
and recur for two cases:

1) The element is included in current combination 
(We put the element in data[] and increment next available index in data[])
2) The element is excluded in current combination 
(We do not put the element and do not change index)

When number of elements in data[] become equal to r 
(size of a combination), we print it.

This method is mainly based on Pascal’s Identity, i.e. ncr = n-1cr + n-1cr-1

Following is implementation of method 2.

'''
# program to print all combination
# of size r in an array of size n
# the main function that prints all
# combinations of size r in arr[] of
# size n. this function mainly uses combinationutil()
# def printcombination(arr,n,r):
#     # a temporary array to store 
#     # all combination one by one
#     data = [0]*r

#     # print all combination using 
#     # temprary array data[]
#     combinationutil(arr,n,r,0,data,0)
#     # arr[] --> input array
#     # n ------> size of input array
#     # index --> current index in data
#     # r ------> size of a combinaion to be printed
#     # data[] -> temporary array to store current combination
#     # i ------> index of current element in arr[]

# def combinationutil(arr,n,r,index,data,i):
#     # current cobination is ready print it

#     if (index == r):
#         for j in range(r):
#             print(data[j], end=' ')
#         print()
#         return
        
#     # wherw no more elements are 
#     # there to put in data
#     if (i>=n):
#         return
    
#     # current is included, put
#     # next at next loacation
#     data[index] = arr[i]
#     combinationutil(arr,n,r,index+1,data,i+1)

#     # current is excluded, put
#     # next at next loacation
#     data[index] = arr[i]
#     combinationutil(arr,n,r,index+1,data,i+1)
    
#     # current is excluded, replace it
#     # with next (note that i+1 is passed
#     # but index is not changed)
#     combinationutil(arr,n,r,index,data,i+1)

# # Driver code
# if __name__ == "__main__":
#     arr = [1,2,3,4,5]
#     r = 3
#     n = len(arr)
#     printcombination(arr,n,r)


def PRINTCOMBINATION(ARR,N,R):

    DATA = [0]*R

    COBINATIONUTIL(ARR,N,R,0,DATA,0)

def COBINATIONUTIL(ARR,N,R,INDEX,DATA,I):

    if (INDEX == R):
        for J in range(R):
            print(DATA[J],end=' ')
        print()
        return

    if (I >= N):
        return

    DATA[INDEX] = ARR[I]
    COBINATIONUTIL(ARR,N,R,INDEX+1,DATA,I+1)
    COBINATIONUTIL(ARR,N,R,INDEX,DATA,I+1)

# DRIVER CODE
if __name__ == '__main__':
    ARR = [1,2,3]
    R = 2
    N = len(ARR)
    PRINTCOMBINATION(ARR,N,R)

