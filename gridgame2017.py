class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        preFix1 = grid[0].copy()
        preFix2 = grid[1].copy()
        result = float("inf")

        for i in range(1, N, 1):
            preFix1[i] = preFix1[i-1] + preFix1[i]
            preFix2[i] = preFix2[i-1] + preFix2[i]

        for i in range(0, N, 1):
            top = preFix1[-1] - preFix1[i]
            if i > 0:
                bot = preFix2[i-1]
            else:
                bot = 0

            secondRobotMax = max(top, bot)
            result = min (secondRobotMax, result)
        return result