class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
         s=0
         for x in nums:
                if nums.count(x) == 1:
                    s = s + x
         return s
         
        