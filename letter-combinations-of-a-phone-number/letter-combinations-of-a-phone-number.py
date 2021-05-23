class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num = {2:'abc', 3:'def', 4:'ghi', 5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        if not digits:
            return []
        res = [r for r in num[int(digits[0])]]
        if len(digits) == 1:
            return res
        for s in digits[1:]:
            t = num[int(s)]
            l = []
            for j in t:
                l += [r+j for r in res]
            res = l
        return sorted(res)
        