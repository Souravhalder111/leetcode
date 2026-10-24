class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        frequency_array = [0] * (n+1)

        for num in nums:
            if(num > 0 and num <= n):
                frequency_array[num] = 1
        
        for i in range(1, n+1):
            if(frequency_array[i] == 0):
                return i
        
        return n+1