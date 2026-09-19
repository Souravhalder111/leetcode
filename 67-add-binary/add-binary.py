class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(a == b == "0"):
            return "0"
        n1 = len(a)
        n2 = len(b)
        num1 = 0
        num2 = 0

        for i in range(n1):
            num1 += int(a[n1-i-1]) * (2**i)
        
        for j in range(n2):
            num2 += int(b[n2-j-1]) * (2**j)

        result_in_decimal = num1 + num2
        result_in_binary = ""

        while(result_in_decimal > 0):
            result_in_binary = str(result_in_decimal % 2) + result_in_binary
            result_in_decimal //= 2
        
        return result_in_binary