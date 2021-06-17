'''
Quick Sort
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 
It picks an element as pivot and partitions the given array 
around the picked pivot. There are many different versions of 
quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.

The key process in quickSort is partition(). 
Target of partitions is, given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all smaller elements 
(smaller than x) before x, and put all greater elements (greater than x) after x. 
All this should be done in linear time.

'''
# program for implementation of Quicksort Sort
# this function takes at its correct position in sorted
# array, and place all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot

# def partition(arr,low,high):
#     i = (low-1) # index of smaller element
#     pivot = arr[high] # pivot 

#     for j in range(low, high):

#         # if current element is smaller than the pivot
#         if arr[j] < pivot:

#             # increment index of smaller element
#             i = i+   1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1] 
#     return (i+1)


# # the main function that implements Quicksort
# # arr[] = array to be sorted
# # low = starting index
# # high = ending index

# def quickSort(arr,low,high):
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr,low,high)

#         # separately sort element before
#         # partition and after partition 
#         quickSort(arr,low,pi-1)
#         quickSort(arr, pi+1, high)

# # Driver code to test above
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr,0,n-1)
# print('sorted array is: ')
# for i in range(n):
#     print("%d" %arr[i],end=' ')


def partition(arr,low,high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_Sort(arr,low, high):
    if low < high:
        pi = partition(arr,low,high)
        quick_Sort(arr,low,pi-1)
        quick_Sort(arr,pi+1,high)
        


arr = [10,7,8,9,1,5]
n = len(arr)
quick_Sort(arr,0,n-1)
for i in range(n):
    print("%d" %arr[i],end=" ")

# Time complexity of QuikSort is O(n2)