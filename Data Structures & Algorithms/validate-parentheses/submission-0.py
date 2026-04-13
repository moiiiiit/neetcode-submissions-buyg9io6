class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if stack:
                if stack[-1] == '[' and char == ']':
                    stack.pop()
                    continue
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                    continue
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                    continue
            stack.append(char)
        return False if stack else True