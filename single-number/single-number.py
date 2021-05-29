class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        for num in hmap:
            if hmap[num] == 1:
                return num
