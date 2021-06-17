'''
code for k largest elements in an array

'''

def klargest(arr,k):
    # sort the given array arr in reverse 
    # order 
    arr.sort(reverse = True)
    # print the first largest elements
    for i in range(k):
        print(arr[i], end=' ')


arr =  [1,3,4,2]
k = 2
klargest(arr,k)


print("\n")
def klargest2(arr,k):
    arr.sort(reverse=True)

    return arr[k]

if __name__ == '__main__':
    arr = [1,3,4,2]
    k = 2
    print(klargest2(arr,k))


# numbers = [1, 3, 4, 2] 
  
# # Sorting list of Integers in descending 
# numbers.sort(reverse = True) 
  
# print(numbers) 


print("\n")
def klargest3(arr,k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i],end=' ')

if __name__ == '__main__':
    arr = [2,8,0,41,3,8]
    k = 2
    klargest3(arr,k)


# time complexity O(nlogn)
