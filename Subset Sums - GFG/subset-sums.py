#User function Template for python3
class Solution:
    def recurseFunc(self, i, subSum, arr, N, subsetSum):
        #Base Condition
        if i == N:
            subsetSum.append(subSum)
            return
        #Add the element into subset
        self.recurseFunc(i+1, subSum+arr[i], arr, N, subsetSum)
        #Do not add the element into subset
        self.recurseFunc(i+1, subSum, arr, N, subsetSum)
        
	def subsetSums(self, arr, N):
		# code here
		subsetSum = []
		self.recurseFunc(0, 0, arr, N, subsetSum)
		subsetSum.sort()
		return subsetSum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends