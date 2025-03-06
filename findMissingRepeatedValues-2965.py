class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        for i in range(1, len(grid) ** 2 + 1):
            if (i not in freq):
                b = i
            elif (freq[i] == 2):
                a = i

        return [a,b]





# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
#         highestNumber = len(grid) ** 2
#         a = None
#         b = None

#         numbersList = []
#         for i in range(1, highestNumber + 1):
#             numbersList.append(i)

#         print(numbersList)
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 try:
#                     numbersList.remove(grid[i][j])
#                 except ValueError:
#                     a = grid[i][j]

#         b = numbersList[0]
#         return [a,b]