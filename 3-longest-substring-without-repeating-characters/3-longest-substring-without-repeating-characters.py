class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            hset = set()
            for j in range(i, len(s)):
                if s[j] in hset:
                    break
                else:
                    hset.add(s[j])
                maxLen = max(maxLen, len(hset))
        return maxLen