class Solution:
    def isPalindrome(self, x: int) -> bool:
        copied_num = x
        remainder = 0
        reversed_num = 0
        while(copied_num):
            remainder = copied_num % 10
            reversed_num = (reversed_num * 10) + remainder
            copied_num = int(copied_num / 10)
        if(x == reversed_num):
            return True
        else:
            return False