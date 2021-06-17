'''
Given an array of integer elements, the task is to find the range and
coefficient of range of the given array where
range: difference between the maximum value and the minimum value in 
the distribution
coefficient of range: (Max-Min)/(Max+Min)

'''
# implementaion to find range and coefficient of range
# Function to return the minimum element from the array
# def getmin(arr,n):
#     res = arr[0]
#     for i in range(1, n, 1):
#         res = min(res, arr[i])
#     return res

# # function to return the maximum
# # element from the array
# def getmax(arr, n):
#     res = arr[0]
#     for i in range(1,n,1):
#         res = max(res, arr[i])
#     return res

# # function to print the range and coefficient of range in the given array
# def findrangeandcoefficient(arr,n):
#     max = getmax(arr,n)
#     min = getmin(arr,n)
#     range = max - min
#     coeffofrange = range/(max + min)
#     print("Range: ",range)
#     print("coefficent of Range: ",coeffofrange)

# # Driver code 
# if __name__ == '__main__':
#     arr = [5,10,15]
#     n = len(arr)
#     findrangeandcoefficient(arr,n)


def getmin(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res

def getmax(arr,n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res

def Rangecoefficent(arr,n):
    max = getmax(arr,n)
    min = getmin(arr,n)
    range = max-min
    coefficent = range/(max+min)
    print("range is: ",range)
    print("coefficent is:",coefficent)


if __name__ == '__main__':
    arr = [15, 16, 10, 9, 6, 7, 17]
    n = len(arr)
    Rangecoefficent(arr,n)
    