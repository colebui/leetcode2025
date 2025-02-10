class Solution:
    def clearDigits(self, s: str) -> str:
        my_list = []
        for char in s:
            if (char.isdigit() and len(my_list) > 0):
                my_list.pop()
            else:
                my_list.append(char)
        return "".join(my_list)