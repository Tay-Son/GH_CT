import sys

N, M = map(int, sys.stdin.readline().split())

stk_ = []


def func(ptr_curr):
    if len(stk_) == M:
        print(' '.join(map(str, stk_)))
    else:
        if ptr_curr < N:
            stk_.append(ptr_curr + 1)
            func(ptr_curr + 1)
            stk_.pop()
            func(ptr_curr + 1)


func(0)