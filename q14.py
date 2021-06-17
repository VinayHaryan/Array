'''
program to find intersection of 
two sorted arrays
function prints intersection of arr1[] and arr2[]
m is the number of elements in arr1[]
n is the number of elements in arr2[]
'''

# def printintersection(arr1, arr2, m, n):
#     i, j = 0,0
#     while i < m and j < n:
#         if arr1[i] < arr2[j]:
#             i += 1

#         elif arr2[j] < arr1[i]:
#             j += 1

#         else:
#             print(arr2[j])
#             j += 1
#             i += 1

# # driver program to test above function
# arr1 = [1,2,4,5,6]
# arr2 = [2,3,5,7]
# m = len(arr1)
# n = len(arr2)
# printintersection(arr1, arr2, m, n)

def intersection(arr1, arr2, m, n):
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr1[i]:
            j += 1

        else:
            print(arr2[j])
            i += 1
            j += 1

# Driver mode
if __name__ == '__main__':
    arr1 = [1,2,4,5,6]
    arr2 = [2,3,5,7]
    m = len(arr1)
    n = len(arr2)
    intersection(arr1, arr2, m, n)


# Time Complexity O(m+n)
