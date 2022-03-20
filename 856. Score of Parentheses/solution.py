class Solution:
    def scoreOfParentheses_mine(self, s: str) -> int:
        stack = []

        for c in s:
            if c == '(': stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    val = stack[-1]
                    while stack[-1] != '(':
                        stack.pop()
                        val *= 2

                    stack.pop()
                    stack.append(val)

                while len(stack) > 1 and stack[-1] != '(' and stack[-2] != '(':
                    val = stack.pop() + stack.pop()
                    stack.append(val)

        return stack[0]

    def scoreOfParentheses_stack(self, s: str) -> int:
        stack = []
        score = 0

        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(2 * score, 1)

        return score

    def scoreOfParentheses(self, s: str) -> int:
        score = depth = 0

        for i, c in enumerate(s):
            if c == '(':
                depth += 1
            else:
                depth -= 1

                if i > 0 and s[i - 1] == '(':
                    score += 2 ** depth

        return score



