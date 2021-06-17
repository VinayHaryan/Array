'''
FIND THE LARGEST THREE DISTINCT ELEMENT IN AN ARRAY

Given an array with all distinct elements, find the largest three elements
Expected time complexity O(n) and extra space O(1)

Examples :

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23

'''
# # Python3 code to find largest
# # three elements in an array
# def find3largest(arr, n):
#     arr = sorted(arr) # It uses Tuned Quicksort with
#                       # avg. case Time complexity = O(nLogn)
 
#     check = 0
#     count = 1
 
#     for i in range(1, n + 1):
 
#         if(count < 4):
#             if(check != arr[n - i]):
                 
#                 # to handle duplicate values
#                 print(arr[n - i], end = " ")
#                 check = arr[n - i]
#                 count += 1
#         else:
#             break
 
# # Driver code
# arr = [12, 45, 1, -1, 45, 54, 23, 5, 0, -10]
# n = len(arr)
# find3largest(arr, n)


def Find3Largest(arr,n):
    arr = sorted(arr)
    check = 0
    count = 0

    for i in range(1,n+1):
        if count < 3:
            if (check != arr[n-i]):
                print(arr[n-i], end=' ')
                check = arr[n-i]
                count += 1

        else:
            break

# driver function
if __name__ == '__main__':
    arr = [0,-200,59,50,400,23,500,200,-555]
    n = len(arr)
    Find3Largest(arr,n)

# An efficient way to solve this probleam is to use any O(nLogn) sorting
# algorithm & simply returning the last 3 largest elements


