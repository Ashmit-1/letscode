class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        signs = set(['+', '-', '/', '*'])
        res = 0

        for i in tokens:
            if i in signs:
                num1 = stack.pop()
                num2 = stack.pop()
                print(f"{num2} {i} {num1}")
                if i == '+':
                    stack.append(num1 + num2)
                elif i == '-':
                    stack.append(num2 - num1)
                elif i == '*':
                    stack.append(num1 * num2)
                else:
                    div = int(float(num2) / num1)
                    stack.append(div)
            else:
                stack.append(int(i))
        return stack.pop()

