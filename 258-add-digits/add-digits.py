class Solution:
    def addDigits(self, num: int) -> int:
        seen = set()
        current_num = str(num)

        while current_num not in seen:
            seen.add(current_num)
            summ = 0
            for digit in current_num:
                digit = int(digit)
                summ += digit

            if(summ < 10 and summ >= 0):
                return summ
            
            current_num = str(summ)