class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = {}
        
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key in hashMap:
            if(hashMap[key] > 1):
                return True
        return False