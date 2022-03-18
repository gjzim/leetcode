class Solution:
    def minRemoveToMakeValid_alt(self, s: str) -> str:
        stack, out = [], ''

        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            elif c == ')':
                if not stack or stack[-1][0] != '(':
                    stack.append((c, i))
                else:
                    stack.pop()        

        j = 0
        for i, c in enumerate(s):
            if j < len(stack) and i == stack[j][1]:
                j += 1
                continue

            out += c

        return out

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        while stack:
            s[stack.pop()] = ''

        return ''.join(s)
