"""
Authors: Deepesh K, Dhaiwat K
Creation date: 09/03/2025
Stock Trading
"""


def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


def main():
    print("Test 1:", maxProfit([7, 1, 5, 3, 6, 4]) == 5)  # Buy at 1, sell at 6
    print("Test 2:", maxProfit([7, 6, 4, 3, 1]) == 0)  # Always falling
    print("Test 3:", maxProfit([1, 2, 3, 4, 5]) == 4)  # Buy at 1, sell at 5
    print("Test 4:", maxProfit([5]) == 0)
    print("Test 5:", maxProfit([]) == 0)
    print("Test 6:", maxProfit([3, 2, 6, 1, 4]) == 4)  # Buy at 2, sell at 6
    print("Test 7:", maxProfit([2, 4, 1, 7]) == 6)  # Buy at 1, sell at 7

if __name__ == "__main__":
    main()