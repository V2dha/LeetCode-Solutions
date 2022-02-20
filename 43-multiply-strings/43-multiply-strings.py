class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Used Hashing
        Time Complexity = O(N)
        """
        def convert_int(num):
            dnum = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
            number = 0
            for i in range(len(num)):
                number += dnum[num[i]]*(10**(len(num)-i-1))
            return number       
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        int_n1 = convert_int(num1)
        int_n2 = convert_int(num2)
        output = int_n1*int_n2
        return str(output)
    
    
        
        