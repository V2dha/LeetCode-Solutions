class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if(len(strs) == 0):
            return prefix
        comparisonWord = strs[0]
        for i in range(len(comparisonWord)):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if comparisonWord[i] != strs[j][i]:
                        return prefix
                else:
                    return prefix
            prefix += comparisonWord[i]
        return prefix
                
