class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0

        for i in range(1, n):

            if(nums[i] != nums[j]):
                nums[j+1] = nums[i]
                j += 1
                
        return j+1