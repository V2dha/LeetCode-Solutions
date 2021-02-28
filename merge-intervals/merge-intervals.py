class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])    #sorting the list based on the start element
        result = [intervals[0]]                #Initializing result to store the first interval
        for i in range(1, len(intervals)):  #iterating from second interval to the last interval
		 #if the ending value of the last interval in the result list is less than the start value 
		 #of the ith interval in the intervals list then add the current interval in result
            if result[-1][1] < intervals[i][0]:     
                result.append(intervals[i])
		#if the ending value of the last interval in the result list is greater than the end value
		#of the ith interval in the intervals list then continue iterating the list as it lies between that interval
            elif result[-1][1] > intervals[i][1]:
                continue
		#if the ending value of the last interval in the result is greater than the start value 
		#and less than the end value of the ith interval in the intervals list then replace 
		#the ending value of the last inteval in the result with the ending value 
		#of the ith interval in the intervals list
            else:
                result[-1][1] = intervals[i][1]
        return result