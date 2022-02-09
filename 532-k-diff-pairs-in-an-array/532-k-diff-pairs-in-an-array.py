class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        if k == 0:
            hmap = {}
            for n in nums:
                if n in hmap:
                    hmap[n] += 1
                else:
                    hmap[n] = 1
            
            for n in hmap:
                if hmap[n] >= 2:
                    count += 1
            return count
            
        s = set(nums)
        count = 0
        for n in s:
            if n+k in s:
                count += 1
        return count