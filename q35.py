'''
MININMIZE THE MAXIMUM DIFFERENCE BETWEEN THE HEIGHTS

Given heights of n towers and a value k. We need to either increase 
or decrease height of every tower by k (only once) where k > 0. 
The task is to minimize the difference between the heights of the 
longest and the shortest tower after modifications, and output this difference.

Input  : arr[] = {1, 15, 10}, k = 6
Output :  Maximum difference is 5.
Explanation : We change 1 to 6, 15 to 
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.

Input : arr[] = {1, 5, 15, 10} 
        k = 3   
Output : Maximum difference is 8
arr[] = {4, 8, 12, 7}

Input : arr[] = {4, 6} 
        k = 10
Output : Maximum difference is 2
arr[] = {14, 16} OR {-6, -4}

Input : arr[] = {6, 10} 
        k = 3
Output : Maximum difference is 2
arr[] = {9, 7} 

Input : arr[] = {1, 10, 14, 14, 14, 15}
        k = 6 
Output: Maximum difference is 5
arr[] = {7, 4, 8, 8, 8, 9} 

Input : arr[] = {1, 2, 3}
        k = 2 
Output: Maximum difference is 2
arr[] = {3, 4, 5} 


'''
# program to find the minimum possible difference between maximum
# possible difference between maximum
# and minimum elements when we have to add/subtract every number by k

# modifies the array by subtracting adding k to every element such that the
# difference between maximum and minimum is minimized
# def getMinDiff(arr, n, k): 
  
#     if (n == 1): 
#         return 0
  
#     # Sort all elements 
#     arr.sort()  
  
#     # Initialize result 
#     ans = arr[n-1] - arr[0]  
  
#     # Handle corner elements 
#     small = arr[0] + k  
#     big = arr[n-1] - k  
      
#     if (small > big): 
#         small, big = big, small  
  
#     # Traverse middle elements 
#     for i in range(1, n-1): 
      
#         subtract = arr[i] - k  
#         add = arr[i] + k  
  
#         # If both subtraction and addition 
#         # do not change diff 
#         if (subtract >= small or add <= big): 
#             continue
  
#         # Either subtraction causes a smaller 
#         # number or addition causes a greater 
#         # number. Update small or big using 
#         # greedy approach (If big - subtract 
#         # causes smaller diff, update small 
#         # Else update big) 
#         if (big - subtract <= add - small): 
#             small = subtract  
#         else: 
#             big = add  
      
  
#     return min(ans, big - small)  
  
  
# # Driver function 
# arr = [ 1, 15, 10 ]  
# n = len(arr)  
# k = 6
  
# print("Maximum difference is", getMinDiff(arr, n, k))  
  

def GETMINHIEGHT(ARR,N,K):
    if (N==1):
        return 0

    ARR.sort()

    # INTIALISE RESULT
    ANS = ARR[N-1] - ARR[0]
    
    # CORNER ELEMENT 
    SMALL = ARR[0] + K
    BIG = ARR[N-1] - K

    if SMALL > BIG:
        SMALL,BIG = BIG,SMALL

    #MIDDLE TRAVERSING
    for I in range(1,N-1):
        SUBTRACT = ARR[I] - K
        ADD = ARR[I] + K

        if (SUBTRACT >= SMALL or ADD <= BIG):
            continue

        if (BIG - SUBTRACT <= ADD - SMALL):
            SMALL = SUBTRACT
        else:
            BIG = ADD
    return min(ANS, BIG - SMALL)

# DRIVER FUNCTION
if __name__ == '__main__':
    ARR = [1, 5, 15, 10]
    K = 3
    N = len(ARR)
    print("MAXIMUM DIFFRENCE IS ",GETMINHIEGHT(ARR,N,K))
        
