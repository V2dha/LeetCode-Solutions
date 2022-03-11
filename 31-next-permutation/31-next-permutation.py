class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Time Complexity - O(N) (3*O(N))
        Space Complexity - O(1)
        """
        n = len(nums)
        for i in range(n-2, -2, -1):
            if nums[i] < nums[i+1]:
                break
        if i < 0:
            nums.reverse()
            return 
        else:
            for j in range(n-1,  i, -1):
                if nums[j] > nums[i]:
                    break
            nums[j], nums[i] = nums[i], nums[j]
            l, r = i+1, len(nums)-1  # reverse the second part
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1 ; r -= 1
            