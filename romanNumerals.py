class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D': 500,
            'M': 1000
        }
        sum = 0


        for index in range(len(s)):
            print(index)
            if (index < len(s)-1) and romans[s[index]] < romans[s[index+1]]:
                sum -= romans[s[index]]

            else:
                sum += romans[s[index]]
        return sum