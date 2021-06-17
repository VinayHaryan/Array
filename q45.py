'''
SORT AN ARRAY IN WAVE FORM

given an unsorted array of integers, sort the array into a wave like array.
array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Examples:

 Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 any other array that is in wave form

 Input:  arr[] = {20, 10, 8, 6, 4, 2}
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4} OR
                 any other array that is in wave form

 Input:  arr[] = {2, 4, 6, 8, 10, 20}
 Output: arr[] = {4, 2, 8, 6, 20, 10} OR
                 any other array that is in wave form

 Input:  arr[] = {3, 6, 5, 10, 7, 20}
 Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form

A Simple Solution is to use sorting. First sort the input array, then swap all adjacent elements.

For example, let the input array be {3, 6, 5, 10, 7, 20}. 
After sorting, we get {3, 5, 6, 7, 10, 20}. 
After swapping adjacent elements, we get {5, 3, 7, 6, 20, 10}.

'''

# python function to sort the array arr[0..n-1] in wave form
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[5]

# def sortinwave(arr,n):

#     # sort the array
#     arr.sort()

#     # swap adjacent elements
#     for i in range(0,n-1,2):
#         arr[i], arr[i+1] = arr[i+1], arr[i]


# # Driver program 
# arr = [10,90,49,2,1,5,23]
# sortinwave(arr,len(arr))
# for i in range(0,len(arr)):
#     print(arr[i], end=" ")

def SORTINWAVE(ARR,N):
    ARR.sort()

    for I in range(0,N-1,2):
        ARR[I], ARR[I+1] = ARR[I+1], ARR[I]

# DRIVER MODE
if __name__ == "__main__":
    # ARR = [20,5,6,3,2,20,100,80]
    ARR = [20, 10, 8, 6, 4, 2]

    N = len(ARR)
    SORTINWAVE(ARR,N)
    for I in range(0,N):
        print(ARR[I],end=" ")

'''
The time complexity of the above solution is O(nLogn) 
if a O(nLogn) sorting algorithm like Merge Sort, 
Heap Sort, .. etc is used.

The time complexity of the above solution is O(nLogn) i
f a O(nLogn) sorting algorithm like Merge Sort, Heap Sort, .. etc is used.

This can be done in O(n) time by doing a single traversal 
of given array. The idea is based on the fact that if 
we make sure that all even positioned (at index 0, 2, 4, ..) 
elements are greater than their adjacent odd elements, 
we don’t need to worry about odd positioned element. 
Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

Below are implementations of above simple algorithm.


'''

def sortInWave(arr, n): 
      
    # Traverse all even elements 
    for i in range(0, n, 2): 
          
        # If current even element is smaller than previous 
        if (i> 0 and arr[i] < arr[i-1]): 
            arr[i],arr[i-1] = arr[i-1],arr[i] 
          
        # If current even element is smaller than next 
        if (i < n-1 and arr[i] < arr[i+1]): 
            arr[i],arr[i+1] = arr[i+1],arr[i] 
  
# Driver program 
arr = [10, 90, 49, 2, 1, 5, 23] 
sortInWave(arr, len(arr)) 
for i in range(0,len(arr)): 
    print (arr[i],end=' ')
      
# This code is contributed by __Devesh Agrawal__ 





















