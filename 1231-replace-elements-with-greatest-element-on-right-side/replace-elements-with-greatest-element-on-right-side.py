class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        temp_1 = -1

        for i in range(n-1, -1, -1):
            temp_2 = arr[i]
            arr[i] = temp_1
            temp_1 = max(temp_1, temp_2)
        
        return arr