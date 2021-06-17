# find missing number 2
'''
Aporoach 
the approach remains the same but there can be overflow
if n is large. in order to avoid integer overflow, pick one
number from known numbers and subtract one from given numbers.
this way there won't have integer overflow ever.


Algiruthn
- create a varuabke sum=1 to which will store the missig number and
a counter c=2
- Travese the array from start to end 
- update the value of sum = sum - array[i] + c and update c as
C++ 
- print the missing number as a sum

'''
# def getMissingNo(a,n):
#     i, total = 0,1
#     for i in range(2, n+2):
#         total += i
#         total -= a[i-2]
#     return total

# # Driver code
# arr = [1,2,3,5]
# print(getMissingNo(arr, len(arr)))

def gemissingno(a,n):
    i,total = 0,1
    for i in range(2,n+2):
        total += i
        total -= a[i-2]
    return total

# Driver
if __name__ == '__main__':
    a = [1,2,4,5]
    n = len(a)
    print(gemissingno(a,n))


# Time complexity O(n)
# only one traversal of the array is needed
# Space Complexity O(1)
# No extra space is needed

'''

This method uses the technique of XOR to solve the problem. 

Approach: 
XOR has certain properties 
Assume a1 ^ a2 ^ a3 ^ …^ an = a and a1 ^ a2 ^ a3 ^ …^ an-1 = b
Then a ^ b = an
Algorithm: 
Create two variables a = 0 and b = 0
Run a loop from 1 to n with i as counter.
For every index update a as a = a ^ i
Now traverse the array from start to end.
For every index update b as b = b ^ array[i]
Print the missing number as a ^ b.

'''
def getmissing_method3(a,n):
    x1 = a[0]
    x2 = 1
    for i in range(1,n):
        x1 = x1 ^ a[i]

    for i in range(2, n+2):
        x2 = x2 ^ i

    return x1 ^ x2

print('\n')
# Driver program to test above function
if __name__ == '__main__':
    a = [1,2,3,5,6]
    n = len(a)
    miss = getmissing_method3(a,n)
    print(miss)
# Time Complexity O(n)
# only one traversal of the array is needed
# space Complexity O(1)
# No extra space is needed


print('\n')
'''
this method will work only in python
-take the sum of all elements in the array and subtract 
that from the sum of n+1 elements for eg
-if my elements are li=[1,2,4,5] then take the sum of all
elements in li and subtract that from the sum of len(li)+1 elements.
the following code sowss the demonstration

'''

def germissing3(a,n):
    n_elements_sum = n*(n+1)//2
    return n_elements_sum - sum(a)

# Driver program to test above function
if __name__ == '__main__':
    a = [1,2,4,5,6]
    n = len(a) + 1
    miss = germissing3(a,n)
    print(miss)
    