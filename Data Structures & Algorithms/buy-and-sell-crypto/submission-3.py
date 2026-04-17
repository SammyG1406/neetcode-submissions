class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L, R= 0, 0

        while R < len(prices):
            if prices[R] <= prices[L]:
                L = R
            res = max(res, prices[R] - prices[L])
            R += 1
        return res  

        