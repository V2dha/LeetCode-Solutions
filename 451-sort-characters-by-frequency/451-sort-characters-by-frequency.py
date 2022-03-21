class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        res = ""
        for ch in s:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
        
        hmap = sorted(hmap.items(), key = lambda x:x[1], reverse=True)
        for key, value in hmap:
            res += key*value
        return res