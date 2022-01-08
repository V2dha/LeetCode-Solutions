class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        ans = sorted(hmap.items(), key=lambda x : x[1])
        return ans[-1][0]
        