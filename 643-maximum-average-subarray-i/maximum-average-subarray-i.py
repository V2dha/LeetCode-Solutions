class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -99999999
      
        if len(nums) == k:
            return sum(nums)/k


        # for i in range(len(nums)-k+1):
        #     avg = sum(nums[i:i+k])/k
        #     max_avg = max(max_avg, avg)

        # return max_avg

        ind_sum = sum(nums[:k])

        for i in range(1, len(nums)-k+1):
            max_sum = max(max_sum, ind_sum)
            ind_sum = ind_sum - nums[i-1] + nums[i+k-1]

            max_sum = max(max_sum, ind_sum)
            
        return max_sum/k




        
                
                

        
        