class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Approach - Moore's Voting Algorithm
        1. initialise count and ele and iterate through arr
        2. if count = 0 then ele = current value
        3. if ele = current value, then count+1 else count-1
        4. retunn ele
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        count = 0
        ele = 0
        for i in range(len(nums)):
            if count == 0:
                ele = nums[i]
            if ele == nums[i]:
                count += 1
            else:
                count -= 1
        return ele
    
        # """
        # Approach - Store key value pairs of nums[i] in hmap
        # if the value > n//2 then return key
        # Time Complexity - O(N)
        # Space Complexity - O(N)
        # """
        # if len(nums) == 1:
        #     return nums[0]
        # hmap = {}
        # for num in nums:
        #     if num in hmap:
        #         hmap[num] += 1
        #         if hmap[num] > len(nums)//2:
        #             return num
        #     else:
        #         hmap[num] = 1
        
        # ans = sorted(hmap.items(), key=lambda x : x[1])
        # return ans[-1][0]
        