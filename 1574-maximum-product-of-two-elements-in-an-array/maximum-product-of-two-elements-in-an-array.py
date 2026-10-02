class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        largest = float("-inf")
        second_largest = float("-inf")

        for num in nums:
            if(num > largest):
                second_largest = largest
                largest = num

            elif(num > second_largest):
                second_largest = num
        
        result = (largest - 1) * (second_largest - 1)

        return result