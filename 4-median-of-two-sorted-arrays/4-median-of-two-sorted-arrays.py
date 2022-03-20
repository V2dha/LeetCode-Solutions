class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        num = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                num.append(nums1[i])
                i += 1
            else:
                num.append(nums2[j])
                j += 1
        while i < m:
            num.append(nums1[i])
            i+=1
        while j < n:
            num.append(nums2[j])
            j+=1
        if len(num) %2 == 0:
            return (num[(n+m)//2]+num[(m+n)//2-1])/2
        return num[(m+n)//2]
                
                
                
                
                
        
                
                
                
                
        