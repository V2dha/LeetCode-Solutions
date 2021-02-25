class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        c3 = 0
        c5 = 0
        for i in range(1, n+1):
            c3 += 1
            c5 += 1
            data = ""
            if c3 == 3:
                data += "Fizz"
                c3 = 0
            if c5 == 5:
                data += "Buzz"
                c5 = 0
            if data == "":
                l.append(str(i))
            else:
                l.append(data)
        return l
            
        