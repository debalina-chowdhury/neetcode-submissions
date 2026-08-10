class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'}':'{', ']': '[', ')': '('}
        for i,c in enumerate(s):
            if c in '])}':
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
#O(n), O(n)
                