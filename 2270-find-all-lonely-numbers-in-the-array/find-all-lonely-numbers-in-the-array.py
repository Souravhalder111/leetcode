class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        n = len(nums)
        hashMap = {}
        result = []

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for key in hashMap:
            if(hashMap[key] == 1):
                if(((key-1) not in hashMap) and ((key+1) not in hashMap)):
                    result.append(key)
        
        return result