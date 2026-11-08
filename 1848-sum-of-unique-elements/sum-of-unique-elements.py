class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        result = 0

        for num in freq:
            
            if(freq[num] == 1):
                result += num
        
        return result