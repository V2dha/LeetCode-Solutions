class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Approach - To start filling from end (m+n) pos 
        1. while m and n, if nums1[m-1] > nums2[n-1] then insert it in m+n-1 and m-=1
        2. else the same for nums2 and n-=1
        3. copy remaining ele from nums2 to nums1 (loop 0-n nums1[i] = nums2[i])
        Time Complexity - O(N+M)
        Space Complexity - O(1)
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        for i in range(n):
            nums1[i] = nums2[i]