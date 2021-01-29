class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        str_set = set()
        left = 0 
        right = 0
        max_len = 0
        while(right < len(s)):
            if s[right] not in str_set:
                str_set.add(s[right])
                max_len = max(max_len, len(str_set))
                right += 1
            else:
                str_set.remove(s[left])
                left += 1
                
        return max_len
                
        
        