class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                count += 1
        if count%2 == 0:
            return 1
        else:
            return -1
        