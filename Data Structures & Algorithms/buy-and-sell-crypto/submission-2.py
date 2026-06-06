class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
                continue
            currentProfit = prices[i] - lowestPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit           
        return maxProfit
