def solution(A):
    stack = []
    for i in A:
        stack.append(i)
        # This is implementation of leader
        while len(stack) and stack[-1] != stack[-2]:
            stack.pop()
            stack.pop()
        # At the end we will have the most common element in stack

    if stack:
        cnt = 0
        for index, i in enumerate(A):
            if i == stack[0]:
                cnt += 1
            if cnt > len(A)/2:
                return index
    return -1
