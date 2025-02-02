class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) == 0):
            return True
        #stack method with list
        mydict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for char in s:
            if (char in mydict.values()): #opening bracket
                stack.append(char)
            else: #assume closing
                if (len(stack) != 0 and stack[-1] == mydict[char]):
                    stack.pop()
                else:
                    return False
        if (len(stack) == 0):
            return True
        return False
