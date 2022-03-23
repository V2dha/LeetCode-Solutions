class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hmap = {}
        count = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum == k:
                count += 1
            if prefixSum-k in hmap:
                count += hmap[prefixSum-k]
            if prefixSum in hmap:
                hmap[prefixSum] += 1
            else:
                hmap[prefixSum] = 1
        return count
    
#         csum = 0
#         count = 0
#         hmap = {0:1}
#         for i in range(len(nums)):
#             csum += nums[i]
#             if csum-k in hmap:
#                 count += hmap[csum-k]
#             if csum in hmap:
#                 hmap[csum] += 1
#             else:
#                 hmap[csum] = 1
#         return count
        
        