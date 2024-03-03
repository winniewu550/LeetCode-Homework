class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Sorting the array
        nums.sort()
        
        for i in range(len(nums) - 1):
        # Checking the adjacent element for equality
            if nums[i] == nums[i + 1]:
                return True
        return False

# Test
sol = Solution()
test_array = [1,2,3,1] 
sol.containsDuplicate(test_array)
