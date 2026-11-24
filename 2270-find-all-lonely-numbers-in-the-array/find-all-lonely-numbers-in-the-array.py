class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        n = len(nums)
        frequency_map = {}
        result = []

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        for key in frequency_map:
            if(frequency_map[key] == 1 and (key-1) not in frequency_map and (key+1) not in frequency_map):
                result.append(key)
        
        return result