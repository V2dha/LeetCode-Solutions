class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = []
        for num in nums:
            sqr.append(num*num)
        sqr.sort()
        return sqr
        