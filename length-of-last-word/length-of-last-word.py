class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == " ":
            return 0
        l = list(s.split( ))
        if not l:
            return 0
        return len(l[len(l)-1])
        