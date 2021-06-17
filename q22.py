'''
Find common elements in threesorted arrays
Given three array sorted i non-decreasing order, print all common
elements in these arrays

Input: 
ar1[] = {1, 5, 10, 20, 40, 80} 
ar2[] = {6, 7, 20, 80, 100} 
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
Output: 20, 80

Input: 
ar1[] = {1, 5, 5} 
ar2[] = {3, 4, 5, 5, 10} 
ar3[] = {5, 5, 10, 20} 
Output: 5, 5

A simple solution is to first find intersection of two 
arrays and store the intersection in a temporary array, 
then find the intersection of third array and temporary array. 

Time complexity of this solution is O(n1 + n2 + n3) 
where n1, n2 and n3 are sizes of ar1[], ar2[] and ar3[] respectively.

The above solution requires extra space and two loops, we can find the 
common elements using a single loop and without extra space. 
The idea is similar to intersection of two arrays. 
Like two arrays loop, we run a loop and traverse three arrays. 

Let the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z. We can have following cases inside the loop. 



If x, y and z are same, we can simply print any of them as common
element and move ahead in all three arrays.

Else If x < y, we can move ahead in ar1[] as x cannot be a common element.

Else If x > z and y > z), we can simply move ahead in ar3[] as z cannot be a common element.

'''

# to print common elements in three sorted arrays
def findcommon(arr1,arr2,arr3, n1, n2, n3):
    # initialize starting indexes for arr1[], arr2[] and arr3[]
    i,j,k = 0,0,0

    # iterate trough three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):
        # if x = y and y = z , print any of them and move ahead
        # in all arrays
        if (arr1[i] == arr2[j] and arr2[j] == arr3[k]):
            print(arr1[i])
            i += 1
            j += 1
            k += 1

        # x < y
        elif arr1[i] < arr2[j]:
            i += 1

        # y < z
        elif arr2[j] < arr3[k]:
            j += 1
        
        # we reach here when x > y and z < y, i.e , z is smallest
        else:
            k += 1

# Driver program to check above function
arr1 = [1,5,10,20,40,80]
arr2 = [6,7,20,80,100]
arr3 = [3,4,15,20,30,70,80,120]
n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)
print("COmmon elements are")
findcommon(arr1,arr2,arr3, n1, n2, n3)


print('\n')
def Find_Common(arr1, arr2, arr3, n1, n2, n3):
    i,j,k = 0,0,0
    while(i<n1 and j<n2 and k<n3):
        if (arr1[i] == arr2[j] and arr2[j] == arr3[k]):
            print(arr1[i])
            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr3[k]:
            j += 1

        else:
            k += 1

# Driver function
if __name__ == '__main__':
    arr1 = [1,5,5]
    arr2 = [3,4,5,5,10]
    arr3 = [5,5,10,20]
    n1 = len(arr1)
    n2 = len(arr2)
    n3 = len(arr3)
    Find_Common(arr1, arr2, arr3, n1, n2, n3)

# Time Complexity of this solution is O(n1+n2+n3)

         