class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Approach - Extended Moore's Voting Algorithm (can be max 2 val for < n/3)
        1. Initialise nums1, nums2 and count1, count2 and iterate through array
        2. if nums1 or nums2 = current val then increase count1 or count2
        3. if count1 or count2 = 0 then set nums1 or nums2 to current val and add to count
        4. else decrease both counts
        5. set both counts to 0 and iterate through array again to get final count of both
        6. if nums1 or nums2 > n/3 then append them to ans and return ans
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
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
        