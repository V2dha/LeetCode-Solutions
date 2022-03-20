#Time Complexity = O(n) Space Complexity = O(k)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 2. Using Deque
        1. Initialise deque and res and iterate through first k ele
        2. while q and nums[i] > nums[qi[-1]] then q.pop()
        3. q.append(i)
        4. then iterate through k till len(nums) vals
        5. res.append(nums[q[0]])
        6. while q and q[0] <= i-k then q.popleft() - out of window values
        7. while q and nums[i] > nums[q[-1]] then q.pop()
        8. q.append(i)
        9. after the loop, enter the last window max -> res.append(nums[q[0]])
        10. return res
        Time Complexity - O(N)
        Space Complexity - O(K)
        """
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
        
        
        