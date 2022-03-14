class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
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
                while j+1 < n and nums[j] == nums[j+1]:
                    j += 1
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
        return res
                