class Solution:
    def findLucky(self, arr: list[int]) -> int:
        frequency_array = [0] * 501

        for num in arr:
            if(frequency_array[num] != 0):
                frequency_array[num] += 1
            else:
                frequency_array[num] = 1
        
        for i in range(500, 0, -1):
            if(frequency_array[i] == i):
                return i
        
        return -1