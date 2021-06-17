'''
Move all negtive numbers to beginning and positive to end with constant extra space

An array contains both positive and negative numbers in random order
rearrage the array elements so that all negtive numbers appear before all
positive numbers

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

'''
# all negtive numbers before positive numbers

def rearrage(arr,n):
    j = 0
    for i in range(n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1

    print(arr)


# driver mode
if __name__ == '__main__':
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    n = len(arr)
    rearrage(arr,n)


