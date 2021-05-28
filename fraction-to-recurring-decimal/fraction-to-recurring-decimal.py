class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
            retlist = []
            if (numerator < 0) ^ (denominator < 0) and (numerator != 0):
                retlist.append('-')
            numerator = abs(numerator)
            denominator = abs(denominator)
            retlist.append(str(numerator//denominator))
            if numerator%denominator:
                retlist.append('.')
            hmap = {}
            rem = numerator % denominator
            while  rem and  rem not in hmap:
                hmap[rem] = len(retlist) - 1
                rem = 10 * rem 
                retlist.append(str(rem // denominator))
                rem = rem % denominator
            if rem:
                retlist.insert(hmap[rem]+1, '(')
                retlist.append(')')
            return ''.join(val for val in retlist)
    
      