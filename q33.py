'''
GIVEN AN ARRAY OF SIZE N AND A NUMBER K,
FIND ALL ELEMENT THAT APPEAR MORE THAN N/K TIMES

given an array of array of size n, find all elements in array that
appear more than n/k times.
for example, if the input array is {3,1,2,2,1,2,3,3} and k is 4
then the output should be [2,3] note that size of array is 8 (or n=8)
so we need to find all elements that appear more than 2 (or 8/4) times.
there are two elements that appear more than two times, 2 and 3

HASHING
can also be can an efficient solution. with a good hash function,
we can solve the above probleam O(n) time on average. extra space required
hashing would be higher than O(k). also, hashing cannot be used to slove
the above variations with O(1) extra space

'''
# code to find element whose 
# frequency yis more than n/k

# def morethanbyk(arr,n,k):
#     x = n/k
#     # unorder_map initixation
#     freq = {}

#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]] += 1
#         else:
#             freq[arr[i]] = 1

#     print(fr)
#     # traversing the map
#     for i in freq:
#         # checking if value of key-value pair 
#         # is greater than x (where x = n/k)
#         if freq[i] > x:
#             # print the key of whose value
#             # is greater than x
#             print(i)

# # driver code
# arr = [1,1,2,2,3,5,4,2,2,3,1,1,1]
# n = len(arr)
# k = 4
# morethanbyk(arr,n,k)


def MORETHANNBYK(ARR,N,K):
    X = N//K
    # MAP INTIALIZATION
    FREQ = {}
    for I in range(N):
        if ARR[I] in FREQ:
            FREQ[ARR[I]] += 1
        else:
            FREQ[ARR[I]] = 1
    print(FREQ)

    # TRAVERSING MAP
    for I in FREQ:
        if FREQ[I] > X:
            print(I)
# DRIVER FUNCTION
ARR = [1,1,2,2,3,5,4,2,2,3,1,1,1]
N = len(ARR)
K = 4
MORETHANNBYK(ARR,N,K)

# TIME COMPLEXITY O(N) TIME ON AVERAGE
# O(1)
