'''
find the first repeating element in an array of integers

Given an array of integers, find the first repeating element in it.
we need to find the element that occurs more than onece and whose index of first
occurrence is smallest

Examples: 

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]


a Simple solution is to use two nested loops. the outer loop picks an 
element one by one, the inner loop checks whwther the element is repeated
or not. once we find an element that repeats, we break the loops and print
the element. Time Complexity of this solution is O(n2)

We can Use Sorting to solve the problem in O(nLogn) time. 
Following are detailed steps. 

1) Copy the given array to an auxiliary array temp[]. 
2) Sort the temp array using a O(nLogn) time sorting algorithm. 
3) Scan the input array from left to right. For every element, 
count its occurrences in temp[] using binary search. 
As soon as we find an element that occurs more than once,
we return the element. This step can be done in O(nLogn) time.


We can Use Hashing to solve this in O(n) time on average. 
The idea is to traverse the given array from right to left 
and update the minimum index whenever we find an element that 
has been visited on right side. 

Following is the implementation of this idea.


'''

# find the first repeating element in arr[]
# this function prints the first repeating element in arr[]

def printFirstRepeating(a,n):
    for i in range(n):
        if a.count(a[i]) > 1:
            return a[i]

    return "there is no repetation number"

a = [10,5,3,4,3,5,6]
print(printFirstRepeating(a,len(a)))


print("\ns")
def PrintFirstRepeating(a,n):
    for i in range(n):
        if a.count(a[i]) > 1:
            return a[i]
    return "there are no repetation"
# Driver Function 
if __name__ == '__main__':
    a = [1,2,3,4,5]
    n = len(a)
    print(PrintFirstRepeating(a,n))


