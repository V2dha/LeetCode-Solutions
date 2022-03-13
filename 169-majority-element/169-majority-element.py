class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
                if hmap[num] > len(nums)//2:
                    return num
            else:
                hmap[num] = 1
        
        # ans = sorted(hmap.items(), key=lambda x : x[1])
        # return ans[-1][0]
        