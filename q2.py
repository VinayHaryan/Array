# program to find the minimum (or maximum) element of an array


# minimum finction
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


# driver mode
if __name__ == "__main__":
    arr = [110,22,3,100,2000]
    n = len(arr)
    print("max element of an array: ", getmax(arr,n))
    print("min element of an array: ", getmin(arr,n))
    
