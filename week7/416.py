class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        summ = sum(nums)
        
        if summ & 1:
            return False
        return self.knapsack_(nums, summ // 2)

    def knapsack_(self, nums, subsetSum):
    # dp[i] := True if i can be formed by nums so far
        dp = [False] * (subsetSum + 1)
        dp[0] = True

        for num in nums:
            for i in range(subsetSum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[subsetSum]