
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #NlogN
        # nums.sort()
        # return nums[len(nums)-k]
        #Nlogk
        return heapq.nlargest(k, nums)[-1]
    
    
        