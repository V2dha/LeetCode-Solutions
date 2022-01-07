#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
        hmap = {}
        res = ""
        for ch in S:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
                res += ch
                
        return res
                
                
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends