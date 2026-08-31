class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n <= 0):
            return False
        if(n == 1):
            return True

        result = 1

        while(result <= n):
            if(result == n):
                return True
            else:
                result *= 4

        return False