class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dictionary: save the key as ch: index

        # [left, right]

        left = 0
        best = 0
        last = {}

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            
            last[ch] = right
            best = max(best, right - left + 1)

        return best