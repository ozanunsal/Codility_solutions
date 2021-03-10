CLOSING = {']': '[', ')': '(', '}': '{'}


def solution(S):
    stack = []
    for ch in S:
        if ch in CLOSING:
            if not stack:
                return 0
            last = stack.pop()
            if last != CLOSING[ch]:
                # wrong bracket encountered
                return 0
        else:
            stack.append(ch)
    if stack:
        # there are still opened brackets on a stack
        return 0
    else:
        return 1
