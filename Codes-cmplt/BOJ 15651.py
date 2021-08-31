import sys

N, M = map(int, sys.stdin.readline().split())

stk_ = []


def func(ptr_curr):
    if ptr_curr == M:
        print(' '.join(map(str, stk_)))
    else:
        for idx_ in range(N):
            stk_.append(idx_+1)
            func(ptr_curr+1)
            stk_.pop()


func(0)