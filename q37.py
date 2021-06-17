# code for find the two repeating elements in a array
# def printRepeating(arr,size):
#     count = [0] * size
#     print("repeating elements are ", end="")
#     for i in range(0,size):
#         if (count[arr[i]] == 1):
#             print(arr[i], end = ' ')
#         else:
#             count[arr[i]] = count[arr[i]] + 1

# # driver code
# arr = [4,2,4,5,2,3,1]
# arr_size = len(arr)
# printRepeating(arr,arr_size)


def PRINTREPEAT(ARR,N):
    COUNT = [0] * N
    for I in range(N):
        if COUNT[ARR[I]] == 1:
            print(ARR[I], end=' ')
        else:
            COUNT[ARR[I]] = COUNT[ARR[I]] + 1

# DRIVER FUNCTION


ARR = [1,2,1,3,2]
N = len(ARR)
PRINTREPEAT(ARR,N)