import sys
def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func(n-1) + func(n-2)

input_ = int(sys.stdin.readline())
print(func(input_))