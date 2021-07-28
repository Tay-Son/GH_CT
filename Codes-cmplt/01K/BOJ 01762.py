import sys
import math

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
lst_depth = [-1 for _ in range(N_ + 1)]
lst_ancestors = [[[-1, 0]] for _ in range(N_ + 1)]

for _ in range(N_ - 1):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_a].append((idx_b, weight_))
    grp_[idx_b].append((idx_a, weight_))

stk_ = [(1, 0)]
while stk_:
    idx_, depth_ = stk_.pop()
    lst_depth[idx_] = depth_
    depth_ += 1
    for target_, weight_ in grp_[idx_]:
        if lst_depth[target_] == -1:
            lst_ancestors[target_][0][0] = idx_
            lst_ancestors[target_][0][1] = weight_
            stk_.append((target_, depth_))

ancestors_max = math.floor(math.log2(max(lst_depth)))+1

for idx_b in range(ancestors_max-1):
    for idx_a in range(1, N_ + 1):
        idx_ancestor, weight_ancestor = lst_ancestors[idx_a][idx_b]
        if idx_ancestor != -1:
            idx_ = lst_ancestors[idx_ancestor][idx_b][0]
            weight_ = lst_ancestors[idx_ancestor][idx_b][1] + weight_ancestor
            lst_ancestors[idx_a].append([idx_, weight_])
        else:
            lst_ancestors[idx_a].append([-1, 0])

for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    tot_ = 0
    if lst_depth[idx_a] < lst_depth[idx_b]:
        idx_a, idx_b = idx_b, idx_a
    for cnt_ in range(ancestors_max-1, -1, -1):
        if lst_depth[idx_a] - lst_depth[idx_b] >= 2 ** cnt_:
            idx_a, weight_ = lst_ancestors[idx_a][cnt_]
            tot_ += weight_

    if idx_a != idx_b:
        for cnt_ in range(ancestors_max-1,-1,-1):
            ancestor_a = lst_ancestors[idx_a][cnt_]
            ancestor_b = lst_ancestors[idx_b][cnt_]
            if ancestor_a[0] != -1 and ancestor_a[0] != ancestor_b[0]:
                tot_ += ancestor_a[1] + ancestor_b[1]
                idx_a = ancestor_a[0]
                idx_b = ancestor_b[0]
        tot_ += lst_ancestors[idx_a][0][1]
        tot_ += lst_ancestors[idx_b][0][1]
    print(tot_)
exit()