import sys


def solution(A):
    # write your code in Python 3.6
    n = len(A)
    left = [0] * n
    for i in range(1, n - 1):
        left[i] = max(0, left[i - 1] + A[i])

    right = [0] * n
    for i in range(n - 2, 1, -1):
        right[i] = max(0, right[i + 1] + A[i])

    max_sum = -sys.maxsize
    for i in range(1, n - 1):
        max_sum = max(max_sum, left[i - 1] + right[i + 1])
    return max_sum
