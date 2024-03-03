class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        answer = 0
        end = 0
        farthest = 0

        clips.sort()

        i = 0
        while farthest < time:
            while i < len(clips) and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if end == farthest:
                return -1
            answer += 1
            end = farthest
        return answer
        