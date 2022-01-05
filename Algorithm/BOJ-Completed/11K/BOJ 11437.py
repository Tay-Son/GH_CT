import sys
import math

sys.setrecursionlimit(10 ** 5)

N_ = int(sys.stdin.readline())

grp_ = [[] for _ in range(N_ + 1)]
lst_depth = [-1 for _ in range(N_ + 1)]
lst_ancestors = [[-1] for _ in range(N_ + 1)]

for _ in range(N_ - 1):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

stk_ = [(1, 0)]
while stk_:
    idx_, depth_ = stk_.pop()
    lst_depth[idx_] = depth_
    depth_ += 1
    for each_ in grp_[idx_]:
        if lst_depth[each_] == -1:
            stk_.append((each_, depth_))
            lst_ancestors[each_][0] = idx_

for idx_b in range(math.ceil(math.log2(max(lst_depth)))):
    for idx_a in range(1, N_ + 1):
        ancestor_ = lst_ancestors[idx_a][idx_b]
        if ancestor_ != -1:
            lst_ancestors[idx_a].append(lst_ancestors[ancestor_][idx_b])
        else:
            lst_ancestors[idx_a].append(-1)


def ancestor(idx_, cnt_):
    ptr_ = 0
    for each_ in reversed(list(map(int, bin(cnt_)[2:]))):
        if each_:
            idx_ = lst_ancestors[idx_][ptr_]
        ptr_ += 1
    return idx_


def func(idx_a, idx_b):
    depth_a = lst_depth[idx_a]
    depth_b = lst_depth[idx_b]
    temp_ = depth_a - depth_b
    if temp_ > 0:
        idx_a = ancestor(idx_a, temp_)
    elif temp_ < 0:
        idx_b = ancestor(idx_b, -temp_)

    if idx_a != idx_b:
        for cnt_ in range(len(lst_ancestors[1]) - 1, -1, -1):
            if lst_ancestors[idx_a][cnt_] != -1 and lst_ancestors[idx_a][cnt_] != lst_ancestors[idx_b][cnt_]:
                idx_a = lst_ancestors[idx_a][cnt_]
                idx_b = lst_ancestors[idx_b][cnt_]
        idx_a = lst_ancestors[idx_a][0]
    return idx_a


for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    print(func(idx_a, idx_b))

exit()