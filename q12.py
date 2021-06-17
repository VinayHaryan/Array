'''
    Union and intersection of two sorted arrays

    Given two sorted arrays, find their union and intersection.
Example:

Input : arr1[] = {1, 3, 4, 5, 7}
        arr2[] = {2, 3, 5, 6} 
Output : Union : {1, 2, 3, 4, 5, 6, 7} 
         Intersection : {3, 5}

Input : arr1[] = {2, 5, 6}
        arr2[] = {4, 6, 8, 10} 
Output : Union : {2, 4, 5, 6, 8, 10} 
         Intersection : {6}

'''
# find union of two sorted arrays
# function prints union of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]

# def printUnion(arr1, arr2, m, n):
#     i, j = 0, 0
#     while i < m and j < n:
#         if arr1[i] < arr2[j]:
#             print(arr1[i])
#             i += 1

#         elif arr2[j] < arr1[i]:
#             print(arr2[j])
#             j += 1

#         else:
#             print(arr2[j])
#             j += 1
#             i += 1

#     # print ramining elements of the larger array
#     while i < m:
#         print(arr1[i])
#         i += 1

#     while j < n:
#         print(arr2[j])
#         j += 1

# # Driver program to test above function
# arr1 = [1,2,4,5,6]
# arr2 = [2,3,4,5,6]
# m = len(arr1)
# n = len(arr2)
# printUnion(arr1, arr2, m, n)

def printunion(arr1, arr2, m, n):
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1

        else:
            print(arr2[j])
            j += 1
            i += 1

    # print remaining element form largest array
    while i < m:
        print(arr1[i])
        i += 1
    while j < n:
        print(arr2[j])
        j += 1

# Driver program to test above function
arr1 = [1,2,4,5,6]
arr2 = [2,3,5,7]


# Time Complexity O(m+n)
'''
    handling duplicates in any of the array above code does not handle duplicates
    in any of the array. to handle the duplicates, just check for every
    element whether adjacent elements of this approch
    
'''