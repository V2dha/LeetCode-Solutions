class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Approach - Store key value pairs of nums[i] in hmap
        if the value > n//2 then return key
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
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
        