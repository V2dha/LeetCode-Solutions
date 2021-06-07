import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        return heapq.nlargest(k, nums)[-1]
        
        