class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0

        for i in range(n):
            num += digits[i] * (10**(n-i-1))
        
        num += 1
        num = str(num)
        result = []

        for char in num:
            result.append(int(char))    

        return result