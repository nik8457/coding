class Solution:
    def isValid(self, s: str) -> bool:
        param_dict = {
            ']': '[', ')': '(', '}': '{',
        }
        stack = []
        for i in s:
            if i in param_dict.keys():
                if stack and stack[-1] == param_dict[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return len(stack) == 0

s = Solution()
print(s.isValid('()'))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([])"))
print(s.isValid(")"))

