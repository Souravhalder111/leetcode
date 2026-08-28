class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = 1
        i = 0
        while(result <= n):
            if(2**i == n):
                return True
            else:
                result *= 2
                i += 1
        return False