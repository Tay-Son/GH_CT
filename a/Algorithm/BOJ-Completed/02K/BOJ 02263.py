import sys

sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
lst_io = list(map(int, sys.stdin.readline().split()))
lst_po = list(map(int, sys.stdin.readline().split()))

lst_eo = dict()
for idx_ in range(n):
    lst_eo[lst_io[idx_]] = idx_


def func(s_, e_, o_):
    p_ = lst_po[e_ - o_]
    idx_p = lst_eo[p_]
    print(p_, end=' ')
    if s_ < idx_p:
        func(s_, idx_p - 1, o_)
    if idx_p < e_:
        func(idx_p + 1, e_, o_ + 1)


func(0, n - 1, 0)