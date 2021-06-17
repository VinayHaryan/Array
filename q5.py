# program for modifying selection sort
# so that it become stable
# def stableselectionsort(a,n):

#     # Travese trough all array elements
#     for i in range(n):
#         # find the minimum element in ramaining unsorted array
#         min_idx = i
#         for j in range(i+1, n):
#             if a[min_idx] > a[j]:
#                 min_idx = j
#         # move minimum elemet at current i
#         key = a[min_idx]
#         while min_idx > i:
#             a[min_idx] = a[min_idx - 1]
#             min_idx -= 1
#         a[i] = key

# def printArray(a,n):
#     for i in range(n):
#         print("%d" %a[i], end= ' ')


# # driver code
# a = [4,5,3,2,4,1]
# n = len(a)
# stableselectionsort(a,n)
# printArray(a,n)

def stable_selectionsort(a,n):
    for i in range(n):
        min_idx = IOError
        for j in range(i+1, n):
            if  a[min_idx] > a[j]:
                min_idx = j
        # move minimum element ar current i
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = key

def printArray(a,n):
    for i in range(n):
        print("%d"%a[i],end=' ')

# driver 
if __name__ == "__main__":

    a = [3,4,8,9,5,8]
    n = len(a)
    stable_selectionsort(a,n)
    printArray(a,n)


    