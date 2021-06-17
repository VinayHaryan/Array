'''
Given an array of positive and negative number, arrange them in an
alternate fasion such that every positive number is followed by negative
and vice-versa maintaining the order of appearance

Number of positive and negtive numbers need not be equal. if there are
more positive numbers they appear at the end of the array. if there are more
negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0} 

this questin has been asked at many places the above probleam can be easily 
solved if O(n) extra space is allowed. it become interesting due to the limitations that O(1) 
extra space is allowed. it becomes interesting due to the limitation that O(1) extra space and  order
of appearances

the idea is to process array from to right. while processing, find the
first out of place element in the remaining unprocessed array. an element is out
of place element in the remaining unprocessed array. an element is out of place if it is
negtive and at odd index, or it is positive and at even
index. Once we find an out of place element, we find the first element after
it with opposite sign. We right rotate the subarray between these two
elements (including these two).
Following is the implementation of above idea.  


'''
# program to rearrange positive and negtive integers
# in alternate fashion and maintaining the order of positive 
# and negative numbers

# def rightRotate(arr, n, outofplace, cur):
#     temp = arr[cur]
#     for i in range(cur, outofplace, -1):
#         arr[i] = arr[i-1]
#     arr[outofplace] = temp
#     print(arr)
#     return arr

# def rearrange(arr, n):
#     outofplace = -1
#     for index in range(n):
#         if (outofplace >= 0):
#             # if element at outofplace in
#             # negative and if element at index
#             # is positive we can rotate the 
#             # array to right or if element 
#             # at outofplace place in positive and
#             # if element at index is negtive we
#             # can rotate the array to right
#             if (arr[index] >= 0 and arr[outofplace] < 0) or (arr[index] < 0 and arr[outofplace] >= 0):

#                 arr = rightRotate(arr,n,outofplace,index)
#                 if(index-outofplace >2 ):
#                     outofplace += 2
#                 else:
#                     outofplace = -1

#         if (outofplace == -1):
#             # conditions for A[index] to
#             # be in out of place
#             if (arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1):
#                 outofplace = index
#     print(arr)
#     return arr



# # Driver code
# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# print("given array is: ")
# print(arr)

# print("\nRearranged array is: ")
# print(rearrange(arr, len(arr)))


# print('\n')
# for i in range(1,0,-1):
#     print(i)


def RightRotate(arr, n, outofplace, cur):
    Temp = arr[cur]
    for i in range(cur,outofplace,-1):
        arr[i] = arr[i-1]
    arr[outofplace] = Temp
    return arr

def Rearange(arr,n):
    outofplace = -1
    for index in range(n):
        if outofplace >= 0:
            if arr[index] >= 0 and arr[outofplace] < 0 or arr[index] < 0 and arr[outofplace] >= 0:
                arr = RightRotate(arr,n,outofplace,index)
                if index - outofplace > 2:
                    outofplace += 2
                else:
                    outofplace = -1

        if outofplace == -1:
            if arr[index] >= 0 and index % 2 == 0 or arr[index] < 0 and index % 2 == 1:
                outofplace = index

    return arr

# driver mode
if __name__ == "__main__":

    arr = [-5,-2,5,2,4,7,1,8,0,-8]
    print(arr)
    print("\n")
    n = len(arr)
    print(Rearange(arr,n))


