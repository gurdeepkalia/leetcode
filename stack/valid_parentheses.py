def solution(s):
    close_to_open_map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c in close_to_open_map:
            if stack and stack[-1] == close_to_open_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return not stack
