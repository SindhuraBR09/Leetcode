class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(0,len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
         
        print(dp)
        return  -1 if dp[amount] > amount else dp[amount]
