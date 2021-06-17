'''
FIND THE MINIMUM ELEMENT IN A SORTED AND ROTATED ARRAY

a sorted array is rotated at some unknown point, find the
minimum element in it
the following solution assume that all elements are distinct

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

A simple solution is to traverse the complete array and find a minimum. 
This solution requires O(n) time. 
We can do it in O(Logn) using Binary Search. 
If we take a closer look at the above examples, we can easily figure out the 
following pattern:

A simple solution is to traverse the complete array and find a minimum. 
This solution requires O(n) time. 

We can do it in O(Logn) using Binary Search. If we take a closer look at the above examples,
we can easily figure out the following pattern

# Python program to find minimum element 
# in a sorted and rotated array 
  
def findMin(arr, low, high): 
    # This condition is needed to handle the case when array is not 
    # rotated at all 
    if high < low: 
        return arr[0] 
  
    # If there is only one element left 
    if high == low: 
        return arr[low] 
  
    # Find mid 
    mid = int((low + high)/2) 
  
    # Check if element (mid+1) is minimum element. Consider 
    # the cases like [3, 4, 5, 1, 2] 
    if mid < high and arr[mid+1] < arr[mid]: 
        return arr[mid+1] 
  
    # Check if mid itself is minimum element 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return arr[mid] 
  
    # Decide whether we need to go to left half or right half 
    if arr[high] > arr[mid]: 
        return findMin(arr, low, mid-1) 
    return findMin(arr, mid+1, high) 
  
# Driver program to test above functions 
arr1 = [5, 6, 1, 2, 3, 4] 
n1 = len(arr1) 
print("The minimum element is " + str(findMin(arr1, 0, n1-1))) 
  
arr2 = [1, 2, 3, 4] 
n2 = len(arr2) 
print("The minimum element is " + str(findMin(arr2, 0, n2-1))) 
  
arr3 = [1] 
n3 = len(arr3) 
print("The minimum element is " + str(findMin(arr3, 0, n3-1))) 
  
arr4 = [1, 2] 
n4 = len(arr4) 
print("The minimum element is " + str(findMin(arr4, 0, n4-1))) 
  
arr5 = [2, 1] 
n5 = len(arr5) 
print("The minimum element is " + str(findMin(arr5, 0, n5-1))) 
  
arr6 = [5, 6, 7, 1, 2, 3, 4] 
n6 = len(arr6) 
print("The minimum element is " + str(findMin(arr6, 0, n6-1))) 
  
arr7 = [1, 2, 3, 4, 5, 6, 7] 
n7 = len(arr7) 
print("The minimum element is " + str(findMin(arr7, 0, n7-1))) 
  
arr8 = [2, 3, 4, 5, 6, 7, 8, 1] 
n8 = len(arr8) 
print("The minimum element is " + str(findMin(arr8, 0, n8-1))) 
  
arr9 = [3, 4, 5, 1, 2] 
n9 = len(arr9) 
print("The minimum element is " + str(findMin(arr9, 0, n9-1))) 



how to handle duplicates
the above approch in the worst case (if all the elements are the same) 
takes O(N)
below is the code to handele duplicates in O(logn)


'''

# program to find minimum element in a sorted
# and rotated array contating duplicate elements
# function to find minimum elements
# def findMin(arr, low, high):
#     while (low < high):
#         mid = low + (high - low) // 2

#         if (arr[mid] == arr[high]):
#             high -= 1
#         elif (arr[mid] > arr[high]):
#             low = mid + 1
#         else:
#             high = mid
#     return arr[high]

# # Driver code
# if __name__ == '__main__':
#     arr = [2,1]
#     n = len(arr)
#     print(n-1)
#     print("The minimum element is ", 
#           findMin(arr, 0, n - 1)) 

# print(0 + (1-0)//2)

def FINDMINIMUMARAY(ARR,LOW,HIGH):
    while (LOW < HIGH):
        MID = LOW + (HIGH - LOW) // 2
        if ARR[MID] == ARR[HIGH]:
            HIGH -= 1
        elif ARR[MID] > ARR[HIGH]:
            LOW = MID + 1
        else:
            HIGH = MID
    return ARR[HIGH]

# DRIVER FUNCTION
if __name__ == '__main__':
    ARR = [1,2,3,4]
    LOW = 0
    N = len(ARR)
    HIGH = N - 1
    print(FINDMINIMUMARAY(ARR,LOW,HIGH))



    

