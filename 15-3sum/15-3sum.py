class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach 1 - Two Pointer Approach using Sorting
        1. Sort the array and run loop till n-2 and skip iteration if two consecutive values are equal
        2. assign left as i+1 and right as n-1 then loop while left < right
        3. if the sum of ith, left, right > 0 right -=1 else left += 1
        4. if equal then add to the resultant array, and get rid of duplicate values with fixed ith
        5. while left < right and nums[left] == nums[left+1]
        Time Complexity = O(N*N)
        Space Complexity = O(1)
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: #skip iteration if there are duplicate elements
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp > 0:
                    right -= 1
                elif temp < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    #Get rid of duplicate cases with fixed ith value
                    while left < right and nums[left] == nums[left+1]: #get rid of duplicate elements
                        left += 1
                    while left < right and nums[right] == nums[right-1]: #get rid of duplicate elements 
                        right -= 1
                    left += 1
                    right -= 1
        return res
        # res = set()
        # for i in range(len(nums)-1):
        #     hmap = {}
        #     for j in range(i+1, len(nums)):
        #         x = -(nums[i]+nums[j])
        #         if x in hmap:
        #             res.add(tuple(sorted((x, nums[i], nums[j]))))
        #         else:
        #             hmap[nums[j]] = 1
        # return res

            
        
            
        