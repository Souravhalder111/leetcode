class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        n1 = len(list1)
        n2 = len(list2)
        dictionary = {}

        for i in range(n1):
            for j in range(n2):
                if(list1[i] == list2[j]):
                    dictionary[list1[i]] = i+j
        
        values = list(dictionary.values())
        mini = min(values)
        
        result = []

        for i in dictionary:
            if(dictionary[i] == mini):
                result.append(i)
        
        return result