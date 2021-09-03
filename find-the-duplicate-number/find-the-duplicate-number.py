class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                return num
      