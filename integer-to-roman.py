class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        romans = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        for key, value in romans.items():
            if (num == 0):
                break
            if (num >= value):
                multiples = num//value

                num -= value * multiples
                result = result + key * multiples
        return result
                
