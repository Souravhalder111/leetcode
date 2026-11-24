class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)

        even_idx_sum = 0
        odd_idx_sum = 0

        for i in range(n):
            
            if(i % 2 == 0):
                even_idx_sum += int(num[i])
            else:
                odd_idx_sum += int(num[i])
        
        if(even_idx_sum == odd_idx_sum):
            return True
        else:
            return False