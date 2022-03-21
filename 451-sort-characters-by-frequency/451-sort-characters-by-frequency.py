class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        res = ""
        #O(N)
        for ch in s:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
        #O(NlogN)
        hmap = sorted(hmap.items(), key = lambda x:x[1], reverse=True)
        #O(N)
        return "".join(map(lambda x:x[0]*x[1], hmap))
    
        for key, value in hmap:
            res += key*value
        return res