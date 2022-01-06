class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if not arr:
            return 0
        res = 0
        
        for index in range(1, len(arr)-1):
            if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
                l = r = index
                while l>0 and arr[l] > arr[l-1]:
                    l-=1
                while r<len(arr)-1 and arr[r] > arr[r+1]:
                    r+=1
                res = max(res, (r-l+1))
        return res
        