class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # min_char_right[i] = smallest char in s[i..end]
        min_char_right = [''] * n
        min_char = 'z'
        for i in range(n - 1, -1, -1):
            if s[i] < min_char:
                min_char = s[i]
            min_char_right[i] = min_char

        t = []  # stack for robot buffer
        result = []
        i = 0

        while i < n or t:
            if i < n:
                t.append(s[i])
                i += 1
            # pop from t while top <= smallest remaining char in s or no chars left in s
            while t and (i == n or t[-1] <= min_char_right[i]):
                result.append(t.pop())

        return "".join(result)