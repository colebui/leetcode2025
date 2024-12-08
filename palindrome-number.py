class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy


def test_isPalindrome():
    solution = Solution()

    # Positive test cases
    assert solution.isPalindrome(121) == True 
    assert solution.isPalindrome(1221) == True  
    assert solution.isPalindrome(0) == True 

    # Negative test cases
    assert solution.isPalindrome(-121) == False  
    assert solution.isPalindrome(123) == False 
    assert solution.isPalindrome(10) == False  

    # Edge cases
    assert solution.isPalindrome(1) == True  
    assert solution.isPalindrome(1001) == True  
    assert solution.isPalindrome(1000021) == False  

    print("All test cases passed!")

test_isPalindrome()
