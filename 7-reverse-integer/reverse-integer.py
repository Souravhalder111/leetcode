class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        remainder = 0
        reversed_num = 0
        while(n):
            remainder = n % 10
            reversed_num = (reversed_num * 10) + remainder
            n = int(n / 10)
        if(x < 0):
            reversed_num = - reversed_num
        if(reversed_num < -2**31 or reversed_num > (2**31 - 1)):
            return 0
        return reversed_num