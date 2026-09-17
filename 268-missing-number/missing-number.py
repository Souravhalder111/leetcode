class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        l = [0] * (n+1)

        for i in range(n):
            l[nums[i]] = 1
        
        for i in range(n+1):
            if(l[i] == 0):
                return i
        else:
            return 0
