class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Time Complexity = O(T)
        Space Complexity = O(1)
        """
        if not s:
            return True
        str_ptr = 0
        for letter in t:
            if letter == s[str_ptr]:
                str_ptr += 1
            if str_ptr == len(s):
                return True
        return False