class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket:
                if not stack or stack[-1] != bracket[i]:
                    return False
                stack.pop()
            else:
                return False
        return not stack