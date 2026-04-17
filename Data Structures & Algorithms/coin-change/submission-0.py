class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # an integer array coins
        # return the fewest number of coins i need to make up the amount(target) with the coin
        # denominations
        # assume unlimited number of each coin
        # larger the coin u use, the quick ull get there.
        # using the largest coin would help until u cant

        length = amount + 1
        dp = [length] * length
        dp[0] = 0

        minimum = float("inf")
        for i in range(1, length):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1