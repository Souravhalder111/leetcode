class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        k = 0
        l = 1

        for i in range(n):
            if(nums[i] % 2 == 0):
                result[k] = nums[i]
                k += 2
                
        for i in range(n):
            if(nums[i] % 2 != 0):
                result[l] = nums[i]
                l += 2
        
        return result