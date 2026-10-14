class Solution(object):
    def minPrice(self, prices, discounts):
        prices.sort()
        discounts.sort()
        total = sum(prices)
        for i in range(min(len(prices), len(discounts))):
            total -= prices[len(prices) - 1 - i] * discounts[len(discounts) - 1 - i] / 100.0
        return total