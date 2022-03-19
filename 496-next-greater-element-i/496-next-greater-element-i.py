class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach 1. Brute Force
        Time Complexity - O(N*N)
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
        