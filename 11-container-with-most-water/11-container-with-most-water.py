class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two Pointer Appoach
        Time Complexity =  O(N)
        """
        n = len(height)-1
        left, right  = 0, n
        maxWater = 0
        while left < right:
            l = right - left #Calculate Length which is right - left
            h = min(height[left], height[right]) #Calculate the minimum height between two so water don't spill
            maxWater = max(maxWater, h*l) #maximum of the both areas
            
            if height[left] < height[right]:  #If left side height is less add left
                left+=1
            else:
                right-=1 #else subtract right
        return maxWater
        