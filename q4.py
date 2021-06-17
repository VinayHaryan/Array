# selection sort
# python program for implementation of selection sort
import sys
a = [64,25,12,22,11]

# Traverse through all array elements
for i in range(len(a)):
     
    # find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1,len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
    
    # swap the found minimum element with
    # the first element
    a[i], a[min_idx] = a[min_idx], a[i]

for i in range(len(a)):
    print("%d" %a[i])
        
# Time Complexity O(n^2)

'''
Auxiliary Space O(1)
the good thing about selection sort is it never makes more than O(n) swaps
and can be useful when memory write is a costly operation
'''


