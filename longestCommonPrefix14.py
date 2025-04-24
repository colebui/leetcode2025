class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        i = 0
        while (i < len(strs)):
            word=strs[i]
            i+=1
            if not word.startswith(shortest):
                if (len(shortest) == 1):
                    return ""
                shortest = shortest[:-1]
                i = 0
            
        return shortest