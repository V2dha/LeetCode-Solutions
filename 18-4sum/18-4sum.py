class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach - Using two pointer approach
        1. Sort the array and initialise res to store result
        2. Start the ith loop, declare thirdTarget = target-nums[i]
        3. Start the jth loop from i+1->n, declar secondTarget=thirdTarget-nums[j]
        4. declare l=j+1 and r=n-1 and while l<r, secondTarget<l+r then l+=1
        5. If equal then add quad to res
        6. Take care of duplicates by while l<r and nums[l]=quad[2] or nums[r]=quad[3]
        7. Take care of duplicates for ith and jth loop in start as well
        Time Complexity - O(N^3)
        Space Complexity - O(1)
        """
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            thirdTarget = target - nums[i]
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                secondTarget = thirdTarget - nums[j]
                l = j+1
                r = n-1
                while l < r:
                    twoSum = nums[l] + nums[r]
                    if twoSum < secondTarget:
                        l += 1
                    elif twoSum > secondTarget:
                        r -= 1
                    else:
                        quad = [nums[i], nums[j], nums[l], nums[r]]
                        res.append(quad)
                        while l < r and nums[l] == quad[2]:
                            l+=1
                        while l < r and nums[r] == quad[3]:
                            r-=1
            #     while j+1 < n and nums[j] == nums[j+1]:
            #         j += 1
            # while i+1 < n and nums[i] == nums[i+1]:
            #     i += 1
        return res
                