class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hmap = dict()
        res = []
        
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
                
        sortedHmap = sorted(hmap.items(), key=lambda x: (x[1],-x[0]))
        for num in sortedHmap:
            res.extend(repeat(num[0], num[1]))
        return res
        
        
        