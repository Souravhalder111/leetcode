class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)

        left = 0
        right = n - 1

        while(left < right):
            if(nums[left] % 2 == 0):
                left += 1
            if(nums[right] % 2 == 1):
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
        
        return nums