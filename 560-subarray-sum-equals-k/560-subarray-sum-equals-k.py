class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum = 0
        count = 0
        hmap = {0:1}
        for i in range(len(nums)):
            csum += nums[i]
            if csum-k in hmap:
                count += hmap[csum-k]
            if csum in hmap:
                hmap[csum] += 1
            else:
                hmap[csum] = 1
        return count
        
        