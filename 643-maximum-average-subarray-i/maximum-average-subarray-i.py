class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums)/k

        # O n*k
        # for i in range(len(nums)-k+1):
        #     avg = sum(nums[i:i+k])/k
        #     max_avg = max(max_avg, avg)

        # return max_avg

        ind_sum = sum(nums[:k])
        max_sum = ind_sum

        for i in range(k, len(nums)):
            ind_sum = ind_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, ind_sum)
            
        return max_sum/k




        
                
                

        
        