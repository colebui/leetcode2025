class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxProfit = 0
        while (j < len(prices)):
            if (prices[j] > prices[i]):
                maxProfit = max(maxProfit, prices[j]-prices[i])
            else:
                i = j
            j+=1
        return maxProfit