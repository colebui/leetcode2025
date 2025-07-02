class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if (cleaned == cleaned[::-1]):
            return True
        return False