class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach - Using Binary Search since the array is sorted
        Before single ele, first occ on even and second occ on odd
        After single ele, first occ on add and second occ on even
        So for any even index, if n[i] = n[i+1] then it must lie after index+1
        else it must lie before index 1
        Time Complexity - O(logN)
        Space Complexity - O(1)
        """
        low = 0
        high = len(nums)-1
        while low < high:
            mid = 2*((low+high)//4)   #to ensure mid is even
            if nums[mid] == nums[mid+1]:
                low = mid+2      #element lies after mid
            else:
                high = mid       #element lies before mid
        return nums[high]
            
           
            