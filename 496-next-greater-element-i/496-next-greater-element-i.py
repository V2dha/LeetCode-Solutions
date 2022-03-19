class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach 2. Using hmap and stack
        Time Complexity - O(N+M)
        """
        stack = []
        hmap = {}
        res = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] > stack[-1]:
                stack.pop()
            if stack:
                hmap[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        for num in nums1:
            if num in hmap:
                res.append(hmap[num])
            else:
                res.append(-1)
        return res
        
        """
        Approach 1. Brute Force
        Time Complexity - O(N*M)
        """
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            flag = -1
            for j in range(index+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    flag = 0
                    break
            if flag == -1:
                res.append(-1)
                
        return res
        