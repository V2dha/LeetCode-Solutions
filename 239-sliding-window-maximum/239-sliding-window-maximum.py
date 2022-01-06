#Time Complexity = O(n) Space Complexity = O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        qi = deque()
        
        for i in range(k):
            while qi and nums[i] >= nums[qi[-1]]:
                qi.pop()
            qi.append(i)
            
        for i in range(k, len(nums)):
            res.append(nums[qi[0]])
            
            while qi and qi[0] <= i-k:
                qi.popleft()
            
            while qi and nums[i] >= nums[qi[-1]]:
                qi.pop()
                
            qi.append(i)
        res.append(nums[qi[0]])
        return res
        
        
        