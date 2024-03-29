class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Approach - By comparing the other strings with first string
        Time Complexity - O(N*M) where N = len(str[0]) and M = len(str)
        """
        prefix = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        comparisonWord = strs[0]
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                currentWord = strs[j]
                if i < len(currentWord):
                    if comparisonWord[i] != currentWord[i]:
                        return prefix
                else:
                    return prefix
            prefix += comparisonWord[i]
        return prefix
        