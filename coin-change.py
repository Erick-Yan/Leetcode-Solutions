'''
    My Solution: Use bottom up dynamic programming with memoization of the previous completed steps. We must 
    solve the # of coins at each amount starting from 0 all the way till the amount. Given a sample coin list of 
    [1, 3, 4, 5]. When the amount is 0, the # of coins that can equal to it is 0:
        DP[0] = 0
    When the amount is 1, the # of coins that can equal to it is:
        DP[1]:
            coin: 1 => 1 + DP[1-1] = 1 (We already know DP[0])
        We don't continue onto the other coins since 3, 4, 5 are all > 1.
    When the amount is 2, the # of coins that can equal to it is:
        DP[2]:
            coin: 1 => 1 + DP[2-1] = 2 (We already know DP[1])
    When the amount is 3:
        DP[3]:
            coin: 1 => 1 + DP[3-1] = 3
            coin: 3 => 1 + DP[3-3] = 0
    And so on. Essentially, we are using our previous calculated numbers to for the next iterated calculation.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    dp[i] = min(1+dp[i-j], dp[i])
                
        
        return dp[amount] if dp[amount] < amount + 1 else -1
            