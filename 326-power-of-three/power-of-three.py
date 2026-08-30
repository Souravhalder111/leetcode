class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n <= 0):
            return False
        
        result = 1
        i = 3
        while(result <= n):
            if(result == n):
                return True
            result *= i
        
        return False