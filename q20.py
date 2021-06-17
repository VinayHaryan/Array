# FIND DUPLICATES IN ARRAY
'''
Given an array of n elements that contains elements from 0 to n-1,
with any of these numbers appearing any number of times. find these
repeating numbers in O(n) and using only constant memory space

Example: 

Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6

Explanation: The numbers 1 , 3 and 6 appears more
than once in the array.

Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3

Explanation: The number 3 appears more than once
in the array.

Solution 1:

Approach:The elements in the array is from 0 to n-1 and all of them are positive. So to find out the duplicate elements, a HashMap is required, but the question is to solve the problem in constant space. There is a catch, the array is of length n and the elements are from 0 to n-1 (n elements). The array can be used as a HashMap. 
Problem in the below approach. This approach only works for arrays having at most 2 duplicate elements i.e It will not work if the array contains more than 2 duplicates of an element. For example: {1, 6, 3, 1, 3, 6, 6} it will give output as : 1 3 6 6.
Note: The above program doesn’t handle 0 cases (If 0 is present in array). The program can be easily modified to handle that also. It is not handled to keep the code simple.
In other approaches below, solutions are discussed that prints repeating elements only once.

Algorithm: 
Traverse the array from start to end.
For every element,take its absolute value and if the abs(array[i])‘th element is positive, the element has not encountered before, else if negative the element has been encountered before print the absolute value of the current element.

'''
def printRepeating(arr, size):
    print("the repeating elements are: ")
    for i in range(0,size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=' ')

# driver code
arr = [1,2,3,1,3,6,6]
arr_size = len(arr)
printRepeating(arr, arr_size)


def printingrepeating(arr, size):
    print("teh repeating elements are: ")
    for i in range(0,size):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]

        else:
            print(abs(arr[i]), end=" ")

# Driver code
print("\n")
arr = [1,2,3,1,3,6,6,6]
arr_size = len(arr)
printingrepeating(arr,arr_size)

# Complexity Anaysis:
# Time Complexity O(n), only one traversal is needed, so time complexity is O(n)
# Auxiliary Space O(1), no extra space is required, so space complexity is constant

'''
Alternate Solution: 

Approach: the basic idea is to use a HashMap to solve the
problem but there is a catch, the numbers in the array are from 0 to n-1, and the input
array has length n. so the input array can be used as a HashMap. while
traversing the array, if an element'a' is encountered then increase the value
of a%n'th element by n

Algorithm
1. Travese the given array from start to end
2. For every element in the array increment the arr[i]%n'th element by n
3. Now traverse the array again nad print all those indexs i for which
   arr[i]/n is greater than 1. which guarantees that the number n has been 
   added to that index
4. This approach works because all elements are in the range from 0 to 
   n-1 and arr[i] would be greater than n only if a value “i” has 
   appeared more than once.


'''
print('\ns')
# code to duplicates in O(n)
numRay = [3, 4, 3, 2, 7, 8,2, 3, 2]
arr_size = len(numRay)
for i in range(arr_size):
    x = numRay[i] % arr_size
    numRay[x] = numRay[x] + arr_size

print('the repeating elements are: ')
for i in range(arr_size):
    if (numRay[i] >= arr_size*2):
        print(i, ' ')

'''
Complexity Analysis: 

Time Complexity: O(n). 
Only two traversals are needed. So the time complexity is O(n).
Auxiliary Space: O(1). 
No extra space is needed, so the space complexity is constant.

'''

arr = [2,2,3,4,5,3,2,3,3,6,7]
arr_size = len(arr)
for i in range(arr_size):
    x = arr[i] % arr_size
    arr[x] = arr[x] + arr_size

print('\n')
print("print duplicat")
for i in range(arr_size):
    if arr[i] >= arr_size*2:
        print(i,end=' ')