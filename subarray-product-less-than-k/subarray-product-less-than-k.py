class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        product = 1
        count = 0
        while end < len(nums) and start < len(nums):
            if product*nums[end] < k:
                product *= nums[end]
                count += end - start + 1
                end = end + 1
            else:
                product /= nums[start]
                start = start + 1
        return count
        