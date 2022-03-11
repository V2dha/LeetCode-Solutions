class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Approach - 3 pointer Approach 
        1. Move zeroes to left, ones to middle and twos to right
        2. Initialise low, mid = 0 and high = n-1
        3. While mid <= high, if mid == 0, swap with low and low+=1, mid+=1
        4. if mid == 1, no swap just mid+=1
        5. if mid == 2, swap with high, high -=1
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
                
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        