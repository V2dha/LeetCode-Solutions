class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Approach - There are 3 cases after sorting according to start :
        1. if the end of 1 interval < start of next interval then append that interval  Eg [1,4][5,6]
        2. if the end of 1 interval > end of next interval then continue Eg - [1,8][4,6]
        3. else change the end of 1 interval with end of current interval Eg - [1,3][2,6]
        Time Complexity = O(NLogN) for sorting and O(N) for traversing
        Space Complexity = O(N) to return the answer
        """
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
        