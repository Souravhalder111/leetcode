class Solution:
    def reverse(self, x: int) -> int:
        remainder = 0
        reversed_num = 0

        if(x < 0):
            sign = -1
        else:
            sign = 1

        x = abs(x)
        
        while(x != 0):
            remainder = x % 10
            reversed_num = (reversed_num * 10) + remainder
            x = x // 10
        
        reversed_num *= sign
        
        if(reversed_num > (2**31 - 1) or reversed_num < -(2**31)):
            return 0
        
        return reversed_num