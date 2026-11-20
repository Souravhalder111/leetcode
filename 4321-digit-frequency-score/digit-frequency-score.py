class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sumOfDigits = 0

        while(n > 0):
            sumOfDigits += n % 10
            n = n // 10
        
        return sumOfDigits