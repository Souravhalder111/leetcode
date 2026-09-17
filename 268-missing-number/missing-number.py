class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        xor = 0 ^ n
        
        for i in range(n):
            xor = xor ^ i ^ nums[i]
        
        return xor