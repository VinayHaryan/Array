'''
k'th smallest/largest Element in unsorted array set1
given to find the k'th smallest element in the given array.
it is given that ll array elements are distint
'''
# Method 1 simple solution 
'''
A simple solution to sort the given array using a O(NlogN) sorting
algorithm like merge sort, heap sort, etc and return the element at
index k-1 in the sorted array

Time Complexity of this solution is O(NlogN)
Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 4
Output: 10


'''
# program to find k'th smallest elements
# function to return k'th smallest 
# element in a given array

# def kthsmallest(arr, n, k):
#     # sort the given array
#     arr.sort()

#     # return k'th elements in the
#     # sorted array
#     return arr[k-1]

# if __name__ =='__main__':
#     arr = [7, 10, 4, 3, 20, 15]
#     k = 3
#     n = len(arr)
#     print("k'th smallest element is",kthsmallest(arr,n,k))

def kthsmallestelement(arr,n,k):
    arr.sort()
    return arr[k-1]

if __name__ == '__main__':
    arr = [7, 10, 4, 3, 20, 15]
    n = len(arr)
    k = 3
    print("kth smallest element is: ",kthsmallestelement(arr,n,k))



