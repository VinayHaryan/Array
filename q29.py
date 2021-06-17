'''
FACTORIAL OF A LARGE NUMBER
Factorial of a non-negtive integer, is the multiplication of all integers
smaller than or equal to n. for example factorial of 6*5*4*3*2*1 which is 720

Input : 100
Output : 933262154439441526816992388562667004-
         907159682643816214685929638952175999-
         932299156089414639761565182862536979-
         208272237582511852109168640000000000-
         00000000000000

Input :50
Output : 3041409320171337804361260816606476884-
         4377641568960512000000000000

The following is a detailed algorithm for finding factorial.
factorial(n) 
1) Create an array ‘res[]’ of MAX size where MAX is number of maximum digits in output. 
2) Initialize value stored in ‘res[]’ as 1 and initialize ‘res_size’ (size of ‘res[]’) as 1. 
3) Do following for all numbers from x = 2 to n. 
……a) Multiply x with res[] and update res[] and res_size to store the multiplication result.

How to multiply a number ‘x’ with the number stored in res[]? 
The idea is to use simple school mathematics. We one by one multiply x with every digit of res[]. 
The important point to note here is digits are multiplied from rightmost digit to leftmost digit. 
If we store digits in same order in res[], then it becomes difficult to update res[] without extra space. 
That is why res[] is maintained in reverse way, i.e., digits from right to left are stored.
multiply(res[], x) 
1) Initialize carry as 0. 
2) Do following for i = 0 to res_size – 1 
….a) Find value of res[i] * x + carry. Let this value be prod. 
….b) Update res[i] by storing last digit of prod in it. 
….c) Update carry by storing remaining digits in carry. 
3) Put all digits of carry in res[] and increase res_size by number of digits in carry.

Below is the implementation of the above algorithm. 
NOTE : In the below implementation, maximum digits in the output are assumed as 500. 
To find a factorial of a much larger number ( > 254), increase the size of an array 
or increase the value of MAX.


'''
# # program to compute factorial of big number
# import sys

# # this function finds factorial of large
# # number and prints them
# def factorial(n):
#     res = [None]*500
#     # initialize result 
#     res[0] = 1
#     res_size = 1

#     # apply simple factorial formula 
#     # n! = 1 * 2 * 3 * ... *n
#     x = 2
#     while x <= n:
#         res_size = multiply(x,res,res_size)
#         x = x + 1

#     print("factorial of gevin number is ")
#     i = res_size - 1
#     while i >= 0:
#         sys.stdout.write(str(res[i]))
#         sys.stdout.flush()
#         i = i - 1

# # this function multiplies x with the number 
# # represented by res[]. res_size is size of res[]
# # or numbber of digit in the number represented 
# # by res[]. this function uses simple school 
# # mathematics for multiplication. this function
# # may value of res_size and return the new value
# # of res_size

# def multiply(x, res, res_size):
#     carry = 0 # initiallize carry
#     # one by one multiply n with individual 
#     # digit of res[]
#     i = 0
#     while i < res_size:
#         prod = res[i] *x + carry
#         res[i] = prod % 10 # store last digit of 
#                            # 'prod in res[]
#         #  make sure floorr division is used
#         carry = prod//10 # put rest in carry
#         i = i+1

#     # put carry in res and increase resul size
#     while (carry):
#         res[res_size] = carry % 10
#         # make sure floor division is used 
#         # to avoid floating value 
#         carry = carry // 10
#         res_size = res_size + 1

#     return res_size
# # diriver program 
# factorial(100)
# print('\n')
# print("______________________________________")
# def Factorial(n):
#     r = 1
#     for i in range(1, n+1):
#         r *= i
#     return r


# print(Factorial(100))

def factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
print(factorial(1000))



