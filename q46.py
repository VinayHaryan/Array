'''
TRAPPING RAIN WATER 

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it 
is able to trap after raining.

Examples:  

Input: arr[]   = {2, 0, 2}
Output: 2
Explanation:
The structure is like below
We can trap 2 units of water in the middle gap.

Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7
Explanation:
Structure is like below
We can trap "3 units" of water between 3 and 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6

Explanation:
The structure is like below
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2


Method 2: This is an efficient solution to the above problem.

Approach: In the previous solution, to find the highest bar 
on the left and right, array traversal is needed which reduces 
the efficiency of the solution. To make this efficient one must 
pre-compute the highest bar on the left and right of every bar 
in linear time. Then use these pre-computed values to find the 
amount of water in every array element.

Algorithm: 
1.Create two array left and right of size n. create a variable max_ = INT_MIN.
2.Run one loop from start to end. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign left[i] = max_
3.Update max_ = INT_MIN.
4.Run another loop from end to start. In each iteration update max_ as max_ = max(max_, arr[i]) and also assign right[i] = max_
5.Traverse the array from start to end.
6.The amount of water that will be stored in this column is min(a,b) – array[i],(where a = left[i] and b = right[i]) add this value to total amount of water stored
7.Print the total amount of water stored.

'''
# def findwater(arr,n):

#     # left [i] contains height of tallest bar the
#     # left of i'th bar including itself
#     left = [0]*n

#     # right [i] contains height of tallest bar to
#     # the right of ith bar including itselff
#     right = [0]*n

#     # initiallize result
#     water = 0

#     # fill left array
#     left[0] = arr[0]
#     for i in range(1,n):
#         left[i] = max(left[i-1], arr[i])

#     # fil right array
#     right[n-1] = arr[n-1]
#     for i in range(n-2, -1, -1):
#         right[i] = max(right[i+1],arr[i])

    
#     # calculate the accumulated water element by element
#     # consider the amount of water on i'th bar, the
#     # amount of water accumalated on this particulatr
#     # bar will be equal to min(left[i], right[i]) - arr[i]
#     for i in range(0, n):
#         water += min(left[i], right[i]) - arr[i]

#     return water

# # Driver program 
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# n = len(arr)
# print("Maximum water that can be accumulated is", findwater(arr, n))


def TRAPWATER(ARR,N):
    LEFT = [0]*N
    RIGHT = [0]*N
    WATER = 0
    #FILL LEFT
    LEFT[0] = ARR[0]
    for I in range(1,N):
        LEFT[I] = max(LEFT[I-1],ARR[I])

    #FILL RIGHT
    RIGHT[N-1] = ARR[N-1]
    for I in range(N-2,-1,-1):
        RIGHT[I] = max(RIGHT[I+1],ARR[I])

    # TRAP
    for I in range(0,N):
        WATER += min(LEFT[I],RIGHT[I]) - ARR[I]

    return WATER

# DRIVER MODE
if __name__ == '__main__':
    ARR = [3,0,2,0,4]
    N = len(ARR)
    print("TRAP WATER IS: ",TRAPWATER(ARR,N))

'''
Complexity Analysis: 
Time Complexity: O(n). 
Only one traversal of the array is needed, So time Complexity is O(n).
Space Complexity: O(n). 
Two extra array is needed each of size n.

Space Optimization for above Solution: 

Instead of maintaing two arrays of size n for 
storing left and right max of each element, 
maintain two variables to store the maximum till 
that point. Since water trapped at any element = min(max_left, max_right) 
– arr[i]. Calculate water trapped on smaller element out of A[lo] and 
A[hi] first and move the pointers till lo doesn’t cross hi.


'''