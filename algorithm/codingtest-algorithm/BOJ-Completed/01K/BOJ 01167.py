import sys

V_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(V_ + 1)]
for _ in range(V_):
    lst_input = list(map(int, sys.stdin.readline().split()))
    idx_s = lst_input[0]
    for ptr_ in range(1, len(lst_input) - 1, 2):
        idx_e, distance_ = lst_input[ptr_], lst_input[ptr_ + 1]
        grp_[idx_s].append((idx_e, distance_))
lst_distance = [-1 for _ in range(V_ + 1)]


def dfs_(grp_, idx_c, tot_distance):
    if lst_distance[idx_c] == -1:
        lst_distance[idx_c] = tot_distance
        for idx_target, distance_ in grp_[idx_c]:
            dfs_(grp_, idx_target, tot_distance + distance_)


dfs_(grp_, 1, 0)

max_ = 0
idx_max = 0
for idx_ in range(V_ + 1):
    if lst_distance[idx_] > max_:
        max_ = lst_distance[idx_]
        idx_max = idx_

lst_distance = [-1 for _ in range(V_ + 1)]

dfs_(grp_, idx_max, 0)

print(max(lst_distance))

exit()
