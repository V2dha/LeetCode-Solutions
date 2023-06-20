class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 1 and n == 0:
            return nums1
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
            return nums1
        while m > 0 and n > 0:  #and because both of them should be in range 
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1

        for i in range(n):
            nums1[i] = nums2[i]


       
