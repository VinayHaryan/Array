'''
LONGEST ALTERNATING SUBSEQUENCE

A sequence {x1, x2, .. xn} is alternating sequence if its elements 
satisfy one of the following relations : 

  x1 < x2 > x3 < x4 > x5 < …. xn or 
  x1 > x2 < x3 > x4 < x5 > …. xn

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest subsequence of length 6.

Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest subsequence of length 6.

inc = Length of longest alternative subsequence so far with current 
value being greater than it’s previous value.

dec = Length of longest alternative subsequence so far with current 
value being smaller than it’s previous value.

The tricky part of this approach is to update these two values. 

“inc” should be increased, if and only if the last element in the alternative 
sequence was smaller than it’s previous element.

“dec” should be increased, if and only if the last element in the alternative sequence 
was greater than it’s previous element.

'''

# # program for above approch
# def LAS(arr,n):

#     # 'inc' and 'dec' intialized as 1
#     # as single element is still LAS
#     inc = 1
#     dec = 1

#     # iterate from second element
#     for i in range(1,n):
        
#         if (arr[i] > arr[i-1]):
#             # 'inc' changes iff 'dec'
#             # changes
#             inc = dec + 1

#         elif (arr[i] < arr[i-1]):

#             # 'dec' changes iff 'inc'
#             # changes
#             dec = inc + 1

#     return max(inc, dec)

# # driver code 
# if __name__ == "__main__":
#     arr = [10,22,9,33,49,50,31,60]
#     n = len(arr)
#     # function call
#     print(LAS(arr,n))

def LAS(ARR,N):

    INC = 1
    DEC = 1

    for I in range(1,N):
        
        if(ARR[I] > ARR[I-1]):
            INC = DEC + 1

        elif(ARR[I] < ARR[I-1]):
            DEC = INC + 1

    return max(INC,DEC)

# DRIVER CODE
if __name__ == '__main__':
    ARR = [1,5,4]
    N = len(ARR)
    print(LAS(ARR,N))

    
# TIME COMPLEXITY O(n)
# AUXILARY SPACE O(1)

