# write the program to reverse the array
# given an array (or string), the task is to 


'''
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

'''
# interative way
# iterative python program to revese an array
# function to reverse a[] from  start to end

def reverseLIst(arr,start,end):
    while start < end:
        
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(arr)
    start = 0
    end = len(arr) - 1
    reverseLIst(arr,start,end)
    print(arr)

# Time Complexity O(n)


# Recursively cal revese for rest of the array
def reverselist(arr,start,end):
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]
    reverselist(arr,start+1, end-1)

print("\n")
arr = [1,2,3,4,5,6]
print(arr)
start = 0
end = len(arr) - 1
reverselist(arr,start,end)
print(arr)