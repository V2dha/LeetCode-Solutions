class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         max_sum = max(max_sum, curr_sum)

        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum+nums[i])
            max_sum = max(curr_sum, max_sum)

        return max_sum
