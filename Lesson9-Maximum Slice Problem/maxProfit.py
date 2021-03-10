import sys


def solution(A):
    # write your code in Python 3.6
    min_val = sys.maxsize
    profit = 0
    for i in A:
        min_val = min(min_val, i)
        profit = max(profit, i - min_val)
    return profit
