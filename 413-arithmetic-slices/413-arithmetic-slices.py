class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
    Every digit that gets added to the sequence adds 'n' more possibilities to the output where 'n' is the difference between number of digits in array and 3.

    e.g For [1,2,3] we have [1,2,3]
    For [1,2,3,4] we have [1,2,3], [1,2,3,4], [2,3,4] ie it adds 2 new sub-arrays ending with 4.
    For [1,2,3,4,5], we have [1,2,3,4,5], [2,3,4,5], [3,4,5] ie it adds 3 new sub-arrays ending with 5 to whatever we could make with 4 elements ie [1,2,3,4]
    Likewise for 6 elements, we will have 4 new sub-arrays that'd be added, so on and forth.

    TLDR:

    So the logic is to add 1 to every single element that gets added in the sequence.
        """
        total = 0
        sub = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                sub += 1
                total += sub
            else:
                sub = 0
        return total