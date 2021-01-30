class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        median = 0.00000
        if(length%2 == 0):
            median = (nums[int(length/2)] + nums[int(length/2-1)])/2
        else:
            median = nums[int((length-1)/2)]
        return median