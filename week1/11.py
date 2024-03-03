class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0
        l = 0
        r = len(height) - 1

        while l < r:
            minHeight = min(height[l], height[r])
            answer = max(answer, minHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return answer
        