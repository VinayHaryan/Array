'''
Largest sum contiguous Subarray
write an efficient program to find the sum of contiguous subarray within a
one-dimensional array of number which has the largest sum

largest subarray sum probleam

arr = [-2,-3,4,-1,-2,1,5,-3]

2 to 6
4 + (-1) + (-2) + 1 + 5 = 7
maximum contiguous Array sum is 7
'''

# # program to find maximum contiguous subarray
# def maxSubArraySum(a, size):
#     max_so_far = a[0]
#     curr_max = a[0]

#     for i in range(1, size):
#         curr_max = max(a[i], curr_max + a[i])
#         max_so_far = max(max_so_far, curr_max)
#     return max_so_far 

# # Driver function
# if __name__ == '__main__':
#     a  = [-2,-3,4,-1,-2,1,5,-3]
#     print("maximum contiguous sum is", maxSubArraySum(a,len(a)))


def MAXSUBARRAYSUM(ARR,N):
    MAX_SO_FAR = ARR[0]
    CURR_MAX = ARR[0]
    for I in range(1,N):
        CURR_MAX = max(ARR[I],CURR_MAX + ARR[I])
        MAX_SO_FAR = max(CURR_MAX,MAX_SO_FAR)
    return MAX_SO_FAR

# DRIVER FUNCTION
if __name__ == '__main__':
    ARR = [1, -2, -3, 0, 7, -8, -2 ]
    N = len(ARR)
    print(MAXSUBARRAYSUM(ARR,N))