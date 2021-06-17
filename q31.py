'''
LONGEST CONSECUTIVE SUBSEQUENCE

given an array of integers. find the length of the longest sub-sequence
such that elements in the subsequence are consecutive integers, the 
consecutive numbers can be in any order

Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
Output: 4
Explanation: 
The subsequence 1, 3, 4, 2 is the longest 
subsequence of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
Explanation: 
The subsequence 36, 35, 33, 34, 32 is the longest 
subsequence of consecutive elements.

Naive Approach: The idea is to first sort the array and find the 
longest subarray with consecutive elements. 
After sorting the array and removing the multiple occurrences of elements,
run a loop and keep a count and max (both initially zero). 
Run a loop from start to end and if the current element is 
not equal to the previous (element+1) then set the count to 1 else increase 
the count. Update max with a maximum of count and max. 


EFFICIENT SOLUTION
This problem can be solved in O(n) time using an Efficient Solution. 
The idea is to use Hashing. We first insert all elements in a Set. 
Then check all the possible starts of consecutive subsequences.

'''
# # FIND THE LONGEST CONTIGUOUS SUBSEQUENCE

# def findLongestConseqSubseq(arr,n):
#     s = set()
#     ans = 0

#     # hash all the array elements 
#     for ele in arr:
#         s.add(ele)

#     # check each possible sequence from the start
#     # then update optimal length
#     for i in range(n):
#         # if current element is the starting 
#         # element of a sequence 
#         if (arr[i] - 1) not in s:
#             # the check for next elements in the
#             # sequence
#             j = arr[i]
#             while(j in s):
#                 j += 1

#             # update optimal length if this length is more
#             ans = max(ans, j-arr[i])
#     return ans

# # driver code
# if __name__ == "__main__":
#     arr = [1,9,3,10,4,20,2]
#     n = len(arr)
#     print("length of the longest contiguos subsequence is")
#     print(findLongestConseqSubseq(arr,n))

def LONGESTCONTIGUOS(ARR,N):
    ANS = 0
    S = set()
    for ELE in ARR:
        S.add(ELE)

    for I in range(N):
        if (ARR[I]-1 not in S):
            J = ARR[I]
            while (J in S):
                J += 1
            ANS = max(ANS, J - ARR[I])
    return ANS

# DRIVER FUNCTION
ARR = [1,9,3,10,4,20,2]
N = len(ARR)
print("LENGTH OF THE LONGEST CONTIGUOUS SUBSEQUENCE IS = ")
print(LONGESTCONTIGUOS(ARR,N))
