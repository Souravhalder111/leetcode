class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        n1 = len(list1)
        n2 = len(list2)

        dictionary1 = {}
        dictionary2 = {}

        for i in range(n1):
            dictionary1[list1[i]] = i

        for j in range(n2):
            if list2[j] in dictionary1:
                dictionary1[list2[j]] += j
                dictionary2[list2[j]] = j
        
        for i in dictionary1:
            if i not in dictionary2:
                dictionary1[i] = -1
        
        keys = list(dictionary1.values())
        mini = float("inf")

        for num in keys:
            if num < mini and num >= 0:
                mini = num

        result = []

        for i in dictionary1:
            if dictionary1[i] == mini:
                result.append(i)

        return result