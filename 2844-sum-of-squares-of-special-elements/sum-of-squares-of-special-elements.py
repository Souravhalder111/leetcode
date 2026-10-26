class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        indices = []

        for i in range(1, n+1):
            if(n % i == 0):
                indices.append(i)
        
        result = 0

        for index in indices:
            result += nums[index - 1]**2
        
        return result