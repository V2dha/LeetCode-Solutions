class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        nums = dict()
        for ch in s:
            if ch in nums:
                nums[ch] += 1
            else:
                nums[ch] = 1
        ch = ''
        for c, value in nums.items():
            if value == 1:
                ch = c
                break
        for i in range(len(s)):
            if s[i] == ch:
                index = i
        return index
                
        