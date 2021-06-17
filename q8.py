''' find the fequency of a number in an array
    Given an array a[] and an element x, find number of occurrences of x in a[].
    Examples:

Input  : a[] = {0, 5, 5, 5, 4}
           x = 5
Output : 3

Input  : a[] = {1, 2, 3}
          x = 4
Output : 0

'''

# python program to count
# occurances of an
# element in an unsorted array
# def frequency(a,x):
#     count = 0

#     for i in a:
#         if i==x:
#             count += 1
#     return count

# # Driver program 
# a = [0,5,5,5,4]
# x = 5
# print(frequency(a,x))

def frequency(a,x):
    count = 0
    for i in a:
        if i == x:
            count += 1
    return count

a = [0,5,5,5,4]
k = 5
print(frequency(a,k))

# Time Complexity O(n)
# Auxiliary Space O(1)


