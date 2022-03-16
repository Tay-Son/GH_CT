import sys
sys.setrecursionlimit(20)

def func(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * func(n-1)

input_ = int(sys.stdin.readline())
print(func(input_))