# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def solution(tokens):
    stack = []
    operators = {"*", "+", "-", "/"}
    for t in tokens:
        if t in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if t == "*":
                val = int(operand2) * int(operand1)
                stack.append(val)
            if t == "/":
                val = int(operand2) / int(operand1)
                stack.append(val)
            if t == "+":
                val = int(operand2) + int(operand1)
                stack.append(val)
            if t == "-":
                val = int(operand2) - int(operand1)
                stack.append(val)
        else:
            stack.append(t)
    return stack[-1]



