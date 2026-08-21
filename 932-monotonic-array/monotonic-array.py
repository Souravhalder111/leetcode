class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        increasing = True
        decreasing = True
        for i in range(n-1):
            if(nums[i] < nums[i+1]):
                decreasing = False
            if(nums[i] > nums[i+1]):
                increasing = False
        
        if(increasing == False and decreasing == False):
            return False
        else:
            return True