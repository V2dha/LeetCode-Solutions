class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        count1, count2 = 0, 0
        nums1, nums2 = -1, -1
        res = []
        for i in range(len(nums)):
            if nums1 == nums[i]:
                count1 += 1
            elif nums2 == nums[i]:
                count2 += 1
            elif count1 == 0:
                nums1 = nums[i]
                count1 = 1
            elif count2 == 0:
                nums2 = nums[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        count1, count2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == nums1:
                count1 += 1
            elif nums[i] == nums2:
                count2 += 1
                
        if count1 > len(nums)//3:
            res.append(nums1)
        if count2 > len(nums)//3:
            res.append(nums2)
            
        return res
        