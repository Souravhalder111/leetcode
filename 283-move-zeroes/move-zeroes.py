class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0            # Traverse the whole array
        j = 0            # Find the non-zero element

        while(i < n):
            if(nums[i] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

            i += 1