# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stack = []
    blocks = 0
    for i in H:
        while stack and stack[-1] > i:
            stack.pop()

        if not stack or stack[-1] < i:
            stack.append(i)
            blocks += 1

    return blocks
