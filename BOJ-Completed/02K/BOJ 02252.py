import sys
sys.setrecursionlimit(10**5)

N_, M_ = map(int, sys.stdin.readline().split())
lst_visited = [False for _ in range(N_ + 1)]

grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    idx_s, idx_e = map(int, sys.stdin.readline().split())
    grp_[idx_e].append(idx_s)

lst_ = []


def func_(idx_e):
    if not lst_visited[idx_e]:
        for idx_s in grp_[idx_e]:
            func_(idx_s)
        lst_.append(idx_e)
        lst_visited[idx_e] = True


for idx_e in range(1, N_ + 1):
    func_(idx_e)

print(' '.join(map(str, lst_)))

exit()
