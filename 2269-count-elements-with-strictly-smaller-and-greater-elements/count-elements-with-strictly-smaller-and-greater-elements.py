class Solution:
    def countElements(self, nums: list[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        
        count = 0

        for num in nums:
            if(num > mini and num < maxi):
                count += 1
        
        return count