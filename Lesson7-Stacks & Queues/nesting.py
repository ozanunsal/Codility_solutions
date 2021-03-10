# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    cnt = 0
    for i in S:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return 0
    return 1 if cnt == 0 else 0
