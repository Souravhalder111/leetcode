class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current_num = str(n)

        while current_num not in seen:
            seen.add(current_num)
            summ = 0
            for digit in current_num:
                digit = int(digit)
                summ += (digit**2)
                
            if(summ == 1):
                return True
            current_num = str(summ)
            
        return False