# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    fishes, stack = [], []

    for i in range(len(A)):
        fishes.append((B[i], A[i]))

    while fishes:
        if stack and not stack[-1][0] and fishes[-1][0]:
            if stack[-1][1] > fishes[-1][1]:
                fishes.pop()
            else:
                stack.pop()
        else:
            stack.append(fishes.pop())

    return len(stack)
