class Solution:
    def romanToInt(self, s: str) -> int:
        intValue = 0
        romanLen = len(s) - 1
        i = 0
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        while i < romanLen:
            currentInt = values[s[i]]
            nextInt = values[s[i+1]]
            
            if currentInt in (1, 10, 100) and nextInt in (currentInt*5, currentInt*10):
                intValue += nextInt - currentInt
                i += 2
            else:
                intValue += currentInt
                i += 1
                
        if i == romanLen:
            intValue += values[s[i]]
        
        return intValue
