class Solution:
    def recurseUtil(self, nums, res):
        if nums:
            mid = (len(nums)-1)//2
            res.append(nums[mid])
            self.recurseUtil(nums[:mid], res)
            self.recurseUtil(nums[mid+1:], res)
        
    
	def sortedArrayToBST(self, nums):
	    # code here
	    res = []
	    self.recurseUtil(nums, res)
	    return res
	    
	

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends