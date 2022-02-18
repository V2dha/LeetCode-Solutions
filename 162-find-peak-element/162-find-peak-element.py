class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Time Complexity = O(LogN)
        Starting from middle 
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return right
#         """
#         Time Complexity = O(N)
#         Space Complexity = Constant
#         """
#         peak = nums[0]
#         index = 0
#         for i in range(1, len(nums)):
#             if nums[i-1] < nums[i] and nums[i] > peak:
#                 peak = nums[i]
#                 index = i
#         return index
    
        
            
                
        