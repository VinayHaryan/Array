'''
MAJORITY ELEMENT

Write a function which takes an array and prints the majority element 
(if it exists), otherwise prints “No Majority Element”. 
A majority element in an array A[] of size n is an element that appears more than 
n/2 times (and hence there is at most one such element). 

Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
Output : 4
Explanation: The frequency of 4 is 5 which is greater
than the half of the size of the array size. 

Input : {3, 3, 4, 2, 4, 4, 2, 4}
Output : No Majority Element
Explanation: There is no element whose frequency is
greater than the half of the size of the array size.

'''

# python program for finding out majarity
# element in an array

# def findMajority(arr, size):
#     m = {}
#     for i in range(size):
#         if arr[i] in m:
#             m[arr[i]] += 1
#         else:
#             m[arr[i]] = 1

#     count = 0
#     for key in m:
#         if m[key] > size/2:
#             count = 1
#             print("majority found : ",key)
#             break
#     if (count == 0):
#         print("no majority element")

# # Driver code
# arr = [2,2,2,2,5,5,2,3,3]
# n = len(arr)
# findMajority(arr,n)

def GETMEJORITY(ARR,SIZE):
    M = {}
    for I in range(SIZE):
        if ARR[I] in M:
            M[ARR[I]] += 1
        else:
            M[ARR[I]] = 1

    COUNT = 0
    for KEY in M:
        if M[KEY] > SIZE/2:
            COUNT = 1
            print('MEJORITY OF ELEMENT IS: ',KEY)
            break
    if (COUNT == 0):
        print("NO MEJORITY")

# DRIVER MODE
if __name__ == '__main__':
    ARR = [22,22,22,22,55,55,22,33,33]
    SIZE = len(ARR)
    GETMEJORITY(ARR,SIZE)



'''
TIME COMPLEXITY O(n)
ONE TRAVERSAL OF THE ARRAY IS NEEDED, SO THE TIME COMPLEXITY IS LINEAR
AUXILIARY SPACE O(n)
SINCE A HASHMAP LINEAR SPACE
'''