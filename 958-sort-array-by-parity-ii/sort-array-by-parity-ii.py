class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        i = 0
        j = 1

        while(i < n and j < n):
            
            if(nums[i] % 2 == 0):
                i += 2
            
            if(nums[j] % 2 != 0):
                j += 2
            
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums