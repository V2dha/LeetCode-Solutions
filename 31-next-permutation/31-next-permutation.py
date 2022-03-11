class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break
        if k < 0:
            nums.reverse()
            return 
        else:
            for j in range(n-1,  k, -1):
                if nums[j] > nums[k]:
                    break
            nums[j], nums[k] = nums[k], nums[j]
            l, r = k+1, len(nums)-1  # reverse the second part
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1 ; r -= 1
            