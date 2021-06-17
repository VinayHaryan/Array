'''
stoke buy sell to maximize profit

The cost of a stock on each day is given in an array, 
find the max profit that you can make by buying and 
selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, 
the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. 
If the given array of prices is sorted in decreasing order, 
then profit cannot be earned at all.


'''
# Python3 Program to find 
# best buying and selling days
 
# This function finds the buy sell
# schedule for maximum profit
# def stockBuySell(price, n):
     
#     # Prices must be given for at least two days
#     if (n == 1):
#         return
     
#     # Traverse through given price array
#     i = 0
#     while (i < (n - 1)):
         
#         # Find Local Minima
#         # Note that the limit is (n-2) as we are
#         # comparing present element to the next element
#         while ((i < (n - 1)) and
#                 (price[i + 1] <= price[i])):
#             i += 1
         
#         # If we reached the end, break
#         # as no further solution possible
#         if (i == n - 1):
#             break
         
#         # Store the index of minima
#         buy = i
#         i += 1
         
#         # Find Local Maxima
#         # Note that the limit is (n-1) as we are
#         # comparing to previous element
#         while ((i < n) and (price[i] >= price[i - 1])):
#             i += 1
             
#         # Store the index of maxima
#         sell = i - 1
         
#         print("Buy on day: ",buy,"\t",
#                 "Sell on day: ",sell)
         
# # Driver code
 
# # Stock prices on consecutive days
# price = [100, 180, 260, 310, 40, 535, 695]
# n = len(price)
 
# # Fucntion call
# stockBuySell(price, n)
 
# # This is code contributed by SHUBHAMSINGH10

# def maxProfit(prices):
     
#     n = len(prices)
#     cost = 0
#     maxcost = 0
 
#     if (n == 0):
#         return 0
 
#     # Store the first element of 
#     # array in a variable
#     min_price = prices[0]
 
#     for i in range(n):
         
#         # Now compare first element with all
#         # the element of array and find the 
#         # minimum element
#         min_price = min(min_price, prices[i])
 
#         # Since min_price is smallest element 
#         # of the array so subtract with every
#         # element of the array and return the
#         # maxCost
#         cost = prices[i] - min_price
 
#         maxcost = max(maxcost, cost)
 
#     return maxcost
 
# # Driver Code
# prices = [ 100, 180, 260, 310, 40, 535, 695 ]
 
# # Stock prices on consecutive days
# print(maxProfit(prices))

def STOCKPRICE(PRICES):
    N = len(PRICES)
    COST = 0
    MAXCOST = 0

    if (N==0):
        return 0

    MIN_PRICE = PRICES[0]
    
    for I in range(N):
        MIN_PRICE = min(MIN_PRICE, PRICES[I])

        COST = PRICES[I] - MIN_PRICE

        MAXCOST = max(MAXCOST,COST)

    return MAXCOST

#DRIVER CODE
PRICES = [7,1,5,3,6,4]
print(STOCKPRICE(PRICES))

'''
TIME COMPLEXITY O(n)
SPACE COMPLEXITY O(1)


'''