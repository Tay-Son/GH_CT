import sys

sys.setrecursionlimit(10 ** 5)
N = int(sys.stdin.readline())
tre_ = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    tre_[idx_a].append(idx_b)
    tre_[idx_b].append(idx_a)

lst_pr = [0 for _ in range(N + 1)]


def func(start_):
    for chld_ in tre_[start_]:
        if lst_pr[chld_] == 0:
            lst_pr[chld_] = start_
            func(chld_)


func(1)

for idx_ in range(2, N + 1):
    print(lst_pr[idx_])
