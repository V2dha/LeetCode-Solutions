class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        r = 0
        hset = set()
        while r < len(s):
            if s[r] not in hset:
                hset.add(s[r])
                r += 1
            else:
                hset.remove(s[l])
                l += 1
            maxLen = max(maxLen, r-l)
        return maxLen
    
        """
        Approach 1 - by generating all substrings and using set
        1. Initialise maxLen and iterate through the string
        2. Initilaise set and loop from i to end
        4. if s[j] in set then break else add in s[j] in set
        5. Update maxLen by max(maxLen, len(set))
        Time Complexity - O(N*N)
        Space Complexity - O(N)
        """
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