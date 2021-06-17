'''
Find the Missing number

You are given a list of n-1 integers and these integers are in 
the range of 1 to n. there are no duplicates in the list. one
of the integers is missing in the list. write an efficient code
to find the missing integer

Example: 

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
Explanation: The missing number from 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
Explanation: The missing number from 1 to 5 is 4


** method 1: The length of the array is n-1. 
So the sum of all n elements, i.e sum of numbers 
from 1 to n can be calculated using the formula n*(n+1)/2. 
Now find the sum of all the elements in the array and subtract 
it from the sum of first n natural numbers, it will be the value 
of the missing element.

**Algorithm: 
Calculate the sum of first n natural numbers as sumtotal= n*(n+1)/2
Create a variable sum to store the sum of array elements.
Traverse the array from start to end.
Update the value of sum as sum = sum + array[i]
Print the missing number as sumtotal – sum

'''

# # getMissingNo takes list as argument
# def getMissingNo(a):
#     n = len(a)
#     total = (n+1) * (n+2)/2
#     sum_of_a = sum(a)
#     return total - sum_of_a

# # driver program to test the above function
# a = [1,2,4,5,6]
# miss = getMissingNo(a)
# print(miss)

def get_missing(a):
    n = len(a)
    total = (n+1) * (n+2) / 2
    sum_of_a = sum(a)
    return total - sum_of_a

#  Driver Function

a = [1,2,3,4,5,6,8,9]
missing=get_missing(a)
print(missing)

# Time Complexity O(n)
# onaly one traverasal of the array is needed
# Space Complexity O(1)
# No extra space is needed





