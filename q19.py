'''
Count Pairs with given sum
Given an array of integers, and number 'sum', find the
number of pairs of integers in the array whose sum is
equal to 'sum'

Examples
Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)


Input  :  arr[] = {1, 5, 7, -1, 5}, 
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)         


Input  :  arr[] = {1, 1, 1, 1}, 
          sum = 2
Output :  6
There are 3! pairs with sum 2.

'''
# implementation of simple method 
# to find count of pairs with given sum
# return number of pairs in arr[0..n-1]
# with sum equal to 'sum'

def getpairscount(arr,n,sum):
    count = 0  # initialize result

    # consider all possible pairs
    # and check their sums
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count

# Driver function
arr = [1,5,7,-1,5]
n = len(arr)
sum = 6
print("cout of pairs is", getpairscount(arr,n,sum))




def getpaircount(arr,n,sum):
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count

# Driver function
arr = [1,1,1,1]
n = len(arr)
sum = 2
print('\n')
print("count of pairs is", getpaircount(arr,n,sum))

# Time Complexity O(n2)
# auxiliary Space O(1)

'''
Efficient solution -
-A better a map to store frequency of each number in the array.
 (single travesal required)

-in the next traversal, for every element check if it can be combined with 
 any other element (other than itself!)  to give the desired sum. increment 
 the computer accordingly

-after completion of second traversal, we'd have twice the required value stored
 in counter because every pair is counted two times. hence divide
 count by 2 and return

below is the implementation of above idea
'''
import sys
# returns number of pirs in arr[0..n-1]
# with sum equal to 'sum'

print('\n')
def getPairsCount(arr, n, sum):
    m = [0] * 1000

    # store counts of all elements in map m
    for i in range(0,n):
        m[arr[i]] += 1

    twice_count = 0
    # iterate through each element and increment
    # the count (notice that every pair is counted twice)
    for i in range(0,n):
        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is decreased by one such 
        # that the arr(arr[i], arr[i]) pair is not consider

        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twise_count
    return int(twice_count/2)

# Driver function
arr = [1,5,7,-1,5]
n = len(arr)
sum = 6
print("count of pairs is", getPairsCount(arr,n,sum))

  