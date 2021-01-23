class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)-1
        RomanDict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        i=0
        while i < l:
            curr_ele = RomanDict[s[i]]
            next_ele = RomanDict[s[i+1]]
            if curr_ele >= next_ele:
                total+=curr_ele
                i+=1
            else:
                total+=(next_ele-curr_ele)
                i+=2
            
        if i==l:
            total+=RomanDict[s[i]]
        return total
                
        
        
