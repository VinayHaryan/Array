'''
MINIMUM NUMBER OF JUMPS TO REACH END

Given an array of integers where each element represents the max number
of steps that can be made forward from that element. write a function to 
return the minimum number of jumps to reach that element. write a function to
return the minimum number of jumps to reach the end of the array (starting from the first element)
if an element is 0, they cannot move throgh that element. if the is't reachable, return -1

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 -> 9)
Explanation: Jump from 1st element 
to 2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump 
is needed so the count of jumps is 10.

METHOD 2 - DYNAMIC PROGRAMMING

Approach: 

1. In this way, make a jumps[] array from left to right such that jumps[i] indicate the minimum number of jumps needed to reach arr[i] from arr[0].
2. To fill the jumps array run a nested loop inner loop counter is j and outer loop count is i.
3. Outer loop from 1 to n-1 and inner loop from 0 to n-1.
4. if i is less than j + arr[j] then set jumps[i] to minimum of jumps[i] and jumps[j] + 1. initially set jump[i] to INT MAX
5. Finally, return jumps[n-1].

'''

# PROGRAM TO FIND MINIMUM NUMBER OF JUMPS TO REACH END
# returns minimum nuber of jumps to reach arr[n-1] from arr[0]
# def minjumps(arr,n):
#     jumps = [0 for i in range(n)]
#     # print(jumps)

#     if (n==0) or (arr[0] == 0):
#         return float("inf")

#     jumps[0] = 0

#     # find the minimum number of jumps to reach arr[i]
#     # from arr[0] and assign this value to jumps[i]
#     for i in range(1,n):
#         jumps[i] = float('inf')
#         for j in range(i):
#             if (i <= j + arr[j]) and (jumps[j] != float('inf')):
#                 jumps[i] = min(jumps[i], jumps[j] + 1)
#                 break
#     return jumps[n-1]

# # Driver program to test above function
# arr = [1,3,6,1,0,9]
# size = len(arr)
# print('minimum nuber of jums to reach end is ',minjumps(arr,size))

# print(float('inf'))


def FINDMINJUMP(ARR,N):
    JUMPS = [0  for I in range(N)]
    if (N==0) or (ARR[0] == 0):
        return float('inf')

    JUMPS[0] = 0

    for I in range(1,N):
        JUMPS[I] = float('inf')
        for J in range(I):
            if (I <= J + ARR[J]) and (JUMPS[J] != float('inf')):
                JUMPS[I] = min(JUMPS[I], JUMPS[J] + 1)
                break
    return JUMPS[N-1]

# DRIVER FUNCTION
if __name__ == '__main__':
    ARR = [1,3,6,1,0,9]
    N = len(ARR)
    print("MINIMUM JUMPS ARE ",FINDMINJUMP(ARR,N))

                 
# TIME COMPLEXIY O(N^2)

