import sys

N_, M_, V_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_ + 1)]

for _ in range(M_):
    val_a, val_b = map(int, sys.stdin.readline().split())
    grp_[val_a].append(val_b)
    grp_[val_b].append(val_a)

for each_ in grp_:
    each_.sort()

lst_is_visited = [False for _ in range(N_ + 1)]
lst_ans_dfs = []


def dfs_(idx_curr):
    lst_is_visited[idx_curr] = True
    lst_ans_dfs.append(idx_curr)
    for idx_target in grp_[idx_curr]:
        if not lst_is_visited[idx_target]:
            dfs_(idx_target)


dfs_(V_)

ptr_ = 0
lst_is_visited = [False for _ in range(N_ + 1)]
lst_ans_bfs = [V_]
lst_is_visited[V_] = True
while ptr_ < len(lst_ans_bfs):
    idx_curr = lst_ans_bfs[ptr_]
    for idx_target in grp_[idx_curr]:
        if not lst_is_visited[idx_target]:
            lst_ans_bfs.append(idx_target)
            lst_is_visited[idx_target] = True
    ptr_ += 1

print(' '.join(map(str, lst_ans_dfs)))
print(' '.join(map(str, lst_ans_bfs)))

exit()