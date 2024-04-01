class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        dp = [0] * n
        c = 0
        dp[0] = 1

        for i in range(1, n):
            dp[i] = c + dp[i-delay] - dp[i-forget]
            c = dp[i]

        return sum(dp[n-forget:]) % 1000000007