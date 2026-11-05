class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)

        while(a <= b):
            ans = a*a + b*b

            if(ans == c):
                return True
            elif(ans < c):
                a += 1
            else:
                b -= 1
        
        return False