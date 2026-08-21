class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        maxProfit = 0
        for i in range(1, n):
            cost = prices[i] - mini
            maxProfit = max(maxProfit, cost)
            mini = min(mini, prices[i])
        return maxProfit