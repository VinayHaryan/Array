'''
NON-REPEATING ELEMENT

find the first non-repeating element in a given array of itegers

Examples:

Input : -1 2 -1 3 2
Output : 3
Explanation : The first number that does not 
repeat is : 3

Input : 9 4 9 6 7 4
Output : 6

'''
# to print all non repeating elements
def firstnonrepeating(arr,n):
    # insert all array elements in hash table
    mp = {}
    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1
        # print(mp)

    # traverse through map only and
    for x in mp:
        if (mp[x] == 1):
            print(x, end=' ')

# driver code 
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
firstnonrepeating(arr,n)


def FirstNonRepeating(arr,n):
    mp = {}
    for i in range(n):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1

    for x in mp:
        if (mp[x] == 1):
            print(x)

# Driver function
if __name__ == '__main__':
    arr = [-1,2,-1,3,2]
    n = len(arr)
    print('\n')
    FirstNonRepeating(arr,n)


