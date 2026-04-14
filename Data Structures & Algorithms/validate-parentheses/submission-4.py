class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for char in s:
            if char not in m:
                stack.append(char)
            elif not stack or m[char] is not stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0