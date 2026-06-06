class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                currentProfit = prices[j] - prices[i]
                if currentProfit > maxProfit:
                    maxProfit = currentProfit            

        if maxProfit < 0: 
            return 0
        return maxProfit


"""----------------------------------
prices = [10,1,5,6,7,1] | buyIndex=0 | sellIndex = 1 | maxProfit = -9


"""
