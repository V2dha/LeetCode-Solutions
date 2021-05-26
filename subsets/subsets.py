class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        def solve(nums, subset, index):
            ans.append(list(subset))
            for i in range(index, n):
                subset.append(nums[i])
                solve(nums, subset, i+1)
                subset.pop()
            return
        
        solve(nums, [], 0)   
        return ans
        