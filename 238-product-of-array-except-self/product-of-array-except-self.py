class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_array = [1]
        suffix_array = [1] * n
        x, y = 1, 1

        for i in range(1, n):
            x *= nums[i-1]
            prefix_array.append(x)

        for i in range(n-1, 0, -1):
            y *= nums[i]
            suffix_array[i-1] = y
        
        result = []

        for i in range(n):
            result.append(prefix_array[i] * suffix_array[i])
        
        return result