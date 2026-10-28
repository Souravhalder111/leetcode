class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = {}

        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        sorted_dict = sorted(frequency.items(), key = lambda x:x[1], reverse = True)

        result = []
        
        for char, freq in sorted_dict:
            result.append(char * freq)
        
        return "".join(result)