class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curMax, curMin = 1 , 1
        for n in nums:
            if (n == 0):
                curMax, curMin = 1 , 1
                continue
            tmpCurMax = curMax
            curMax = max(tmpCurMax * n, curMin * n, n)
            curMin = min(tmpCurMax * n, curMin * n, n)
            res = max (curMax, res)
        return res