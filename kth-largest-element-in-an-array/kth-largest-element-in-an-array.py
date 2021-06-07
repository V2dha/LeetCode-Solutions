import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = heapq.nlargest(k, nums)
        return n[-1]
        
        