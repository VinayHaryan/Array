# find union of two sorted arrays (handling Duplicates)
def unionAraay(arr1, arr2):
    # taking max element present in either array
    m = arr1[-1]
    n = arr2[-1]
    ans = 0

    if m > n:
        ans = m
    else:
        ans = n

    # finding elements from 1st array
    # (non duplicates only) using
    # another array for sorting union
    # elements of both arrays
    # assuming max element present 
    # in array is not element present 
    # in array is not more than 10^7 


    newtable = [0] * (ans + 1)

    # first element is always
    # present in final answer
    print(arr1[0], end=' ')

    # incrementing the first element's count
    # in it's corresponding index in newtable
    newtable[arr1[0]] += 1

    # starting traversing the first 
    # array from 1st index till last
    for i in range(1, len(arr1)):

        # checking whether current element
        # is not equal to it's previsous element
        if arr1[i] != arr1[i-1]:
            print(arr1[i], end=' ')
            newtable[arr1[i]] += 1

    # finding only non common
    # elements from 2nd array
    for j in range(0, len(arr2)):

        # by checking wether it's already
        # present in newtable or not
        if newtable[arr2[j]] == 0:

            print(arr2[j], end=' ')
            newtable[arr2[j]] += 1

# Driver code
if __name__ == '__main__':
    arr1 = [1,2,2,2,3]
    arr2 = [2,3,4,5]
    unionAraay(arr1, arr2)

print('\nss')

def unionArray(arr1, arr2):
    arr1 = arr1[-1]
    arr2 = arr2[-1]
    ans = 0

    if m > n:
        ans = m
    else:
        ans = n

    newdata = [0] * (ans + 1)
    print(arr1[0], end=' ')
    newdata[arr1[0]] += 1

    for i in range(1, len(arr1)):
        if arr1[i] != arr1[i-1]:
            print(arr1[i], end=' ')
            newdata[arr1[i]] += 1

    for j in range(0, len(arr2)):
        if newdata[arr2[j]] == 0:
            print(arr2[j],end=' ')
            newdata[arr2[j]] += 1

# driver mode
if __name__ == '__main__':
    arr1 = [1,2,2,2,3]
    arr2 = [2,3,4,5]
    unionAraay(arr1, arr2)






