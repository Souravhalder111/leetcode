class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n < 0):
            x = 1 / x
            n = abs(n)
        def power_of_x(x, n):
            if(n == 0):
                return 1
            elif(n % 2 == 0):
                return power_of_x(x*x, int(n/2))
            else:
                return x * power_of_x(x*x, int(n/2))
        
        return power_of_x(x, n)