class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time Complexity - LogN
        Space Complexity - O(1)
        """
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            #left part is sorted
            if nums[low] <= nums[mid]:
                #target lies in the sorted
                if target >= nums[low] and target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            #right part is sorted
            else:
                #target lies in the sorted part
                if target >= nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
                    
        return -1
#         if target in nums:
#             index = nums.index(target)
#             return index
#         return -1
        