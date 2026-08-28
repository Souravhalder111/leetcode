import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number1 = 0
        new_digits = []

        for i in range(n):
            number1 += digits[i] * pow(10, (n-i-1))
        number2 = str(number1 + 1)

        for i in range(len(number2)):
            new_digits.append(int(number2[i]))

        return new_digits