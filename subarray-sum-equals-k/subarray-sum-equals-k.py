class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currsum = 0
        value = {0:1}
        
        for i in range(len(nums)):
            currsum += nums[i]
            if (currsum-k) in value:
                count += value[currsum-k]
            if currsum in value:
                value[currsum] += 1
            else:
                value[currsum] = 1
        
        return count