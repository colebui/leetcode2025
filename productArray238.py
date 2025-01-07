class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array1 = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            array1[i] = prefix
            prefix = nums[i] * prefix
        
        postfix = 1

        for i in range(len(nums) -1, -1, -1):   #start stop step
            array1[i] = postfix * array1[i]
            postfix = postfix * nums[i]

        return array1