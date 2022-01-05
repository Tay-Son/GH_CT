import sys

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_ + 1)]
lst_d = [0 for _ in range(M_ + 1)]
for idx_n in range(1, N_ + 1):
    lst_input = list(map(int, sys.stdin.readline().split()))
    for idx_m in lst_input[1:]:
        grp_[idx_n].append(idx_m)


def func(idx_n):
    if lst_visited[idx_n]:
        return False
    else:
        lst_visited[idx_n] = True
        for idx_m in grp_[idx_n]:
            if lst_d[idx_m] == 0 or func(lst_d[idx_m]):
                lst_d[idx_m] = idx_n
                return True
        return False


answer_ = 0
for idx_n in range(1, N_ + 1):
    lst_visited = [False for _ in range(N_ + 1)]
    if func(idx_n):
        answer_ += 1

print(answer_)

exit()
