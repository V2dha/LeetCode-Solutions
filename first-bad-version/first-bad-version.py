# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = (start+end)//2
            if isBadVersion(mid) == False:
                start = mid+1
            elif isBadVersion(mid):
                if isBadVersion(mid-1):
                    end = mid-1
                else:
                    return mid
            