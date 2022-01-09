class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time Complexity = nlogn Space Complexity = 1
            # for i in range(len(nums)):
            #     nums[i] = nums[i]**2
            # nums.sort()
            # return nums
        
        #Time Complexity = n Space Complexity = n
        res = []
        left, right = 0, len(nums)-1
        
        while left <= right:
            if abs(nums[left]) >= nums[right]:
                res.append(nums[left]**2)
                left += 1
            else:
                res.append(nums[right]**2)
                right -= 1
        
        return res[::-1]
        
                        
        