class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        hashArray = [0] * (n+1)
        result =  []

        for num in nums:

            if(hashArray[num] > 0):
                hashArray[num] += 1
            else:
                hashArray[num] = 1
            
        for i in range(1, n+1):
            
            if(hashArray[i] == 0):
                result.append(i)
        
        return result