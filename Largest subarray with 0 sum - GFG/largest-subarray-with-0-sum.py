#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        """
        Approach 2: Using Hash Map and storing prefixSum
        1. Initialise maxLen, prefixSum and iterate through array
        2. add in prefixSum if prefixSum = 0: then maxLen = i+1
        3. else if prefixSum in hmap then update maxLen
                else add prefixSum as key and index as value in hmap
        Time Complexity - O(N)
        Space Complexity - O(N)
        """
        hmap = {}
        maxLen = 0
        prefixSum = 0
        for i in range(n):
            prefixSum += arr[i]
            if prefixSum == 0:
                maxLen = i+1
            else:
                if prefixSum in hmap:
                    maxLen = max(maxLen, i-hmap[prefixSum])
                else:
                    hmap[prefixSum] = i
        return maxLen
        
        
        
        """
        Approach 1: Brute Force (Check the sum for each subarray)
        1. Initialise a maxLen and iterate through array
        2. Initialise currSum = 0 and iterate through i to n-1
        3. Add into currSum and if it is = 0 then update max(maxLen, j-1+1)
        Time Complexity - O(N*N)
        Space Complexity - O(1)
        """
        maxLen = 0
        for i in range(n):
            currSum = 0
            for j in range(i, n):
                currSum += arr[j]
                if currSum == 0:
                    maxLen = max(maxLen, j-i+1)
        return maxLen
                    
            

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends