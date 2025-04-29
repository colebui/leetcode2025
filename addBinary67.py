class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2) 
        num2 = int(b, 2)   
        total = num1 + num2
        return bin(total)[2:] 


    def addBinary2(a, b):
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            result.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(result))