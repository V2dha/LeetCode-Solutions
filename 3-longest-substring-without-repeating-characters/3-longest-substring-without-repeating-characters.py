class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach 2 - Two Pointer Approach and removing left char from set
        1. Initialise maxLen, l, r and set and iterate while r < len(s)
        2. if s[r] not in set then add into set and r += 1
        3. else remove s[l] from set and l += 1
        4. Update maxLen by max(maxLen, r-l)
        Time Complexity - O(N) (O(2N) since each each value will be visited by l and r)
        Space Complexity - O(N)
        """
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