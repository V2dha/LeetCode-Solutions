class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity = O(2^n)
        Space Complexity = 
        """
        res = []
        self.dfs(candidates, target, [], res)
        return res
    
    def dfs(self, nums, target, path, res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], res)