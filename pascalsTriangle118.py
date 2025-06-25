class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            if i > 0:
                for k in range(1, i):
                    sum = triangle[i-1][k-1] + triangle[i-1][k]
                    row.append(sum)
            
                row.append(1)
            triangle.append(row)

        return triangle