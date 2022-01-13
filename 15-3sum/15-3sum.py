class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-1):
            hmap = {}
            for j in range(i+1, len(nums)):
                x = -(nums[i]+nums[j])
                if x in hmap:
                    res.add(tuple(sorted((x, nums[i], nums[j]))))
                else:
                    hmap[nums[j]] = 1
        return res
            
        