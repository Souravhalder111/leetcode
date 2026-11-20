class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n = len(nums)
        result = []
        countOfPivot = 0

        for i in range(n):
            if(nums[i] < pivot):
                result.append(nums[i])
            if(nums[i] == pivot):
                countOfPivot += 1
        
        while(countOfPivot > 0):
            result.append(pivot)
            countOfPivot -= 1
        
        for i in range(n):
            if(nums[i] > pivot):
                result.append(nums[i])
        
        return result