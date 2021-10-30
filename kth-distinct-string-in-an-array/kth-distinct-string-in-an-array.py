class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = {}
        for string in arr:
            if string in hmap:
                hmap[string] += 1
            else:
                hmap[string] = 1
        
        count = 0
        for string in hmap:
            if hmap[string] == 1:
                count += 1
            if count == k:
                return string
        return ""
        
        