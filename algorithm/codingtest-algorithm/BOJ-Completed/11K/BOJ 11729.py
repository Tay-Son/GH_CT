import sys

N = int(sys.stdin.readline())


def func(s, e, n):
    if n > 1:
        lst_ = ['1', '2', '3']
        lst_.remove(s)
        lst_.remove(e)
        p = lst_[0]
        func(s, p, n - 1)
    print(s + ' ' + e)
    if n > 1:
        func(p, e, n - 1)


print(2**N-1)
func('1', '3', N)