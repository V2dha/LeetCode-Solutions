#Time Complexity = O(n) Space Complexity = O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        qi = deque()
        
        for i in range(k):
            while qi and nums[i] > nums[qi[-1]]:
                qi.pop()
            qi.append(i)
            
        for i in range(k, len(nums)):
            res.append(nums[qi[0]])
            
            #remove the element if its outside the window
            while qi and qi[0] <= i-k:
                qi.popleft()
            
            while qi and nums[i] > nums[qi[-1]]:
                qi.pop()
                
            qi.append(i)
        res.append(nums[qi[0]])
        return res
    
        """
        Approach 1. Brute Force
        Time Complexity - O(N*K)
        Space Complexity - O(1)
        """
        res = []
        for i in range(len(nums)-k+1):
            maxi = nums[i]
            for j in range(i, i+k):
                maxi = max(maxi, nums[j])
            res.append(maxi)
        return res
        
        
        