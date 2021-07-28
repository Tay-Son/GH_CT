import sys
import math

N_ = int(sys.stdin.readline())
lst_depth = [-1 for _ in range(N_ + 1)]
lst_ancestors = [[[-1, 1000000, 0]] for _ in range(N_ + 1)]

grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_a].append((idx_b, weight_))
    grp_[idx_b].append((idx_a, weight_))

stk_ = [(1, 0)]
while stk_:
    idx_subject, depth_ = stk_.pop()
    lst_depth[idx_subject] = depth_
    depth_ += 1
    for idx_target, weight_ in grp_[idx_subject]:
        if lst_depth[idx_target] == -1:
            lst_ancestors[idx_target][0][0] = idx_subject
            lst_ancestors[idx_target][0][1] = weight_
            lst_ancestors[idx_target][0][2] = weight_
            stk_.append((idx_target, depth_))

ancestors_max = math.floor(math.log2(max(lst_depth))) + 1
for idx_b in range(ancestors_max - 1):
    for idx_a in range(1, N_ + 1):
        idx_anc1, min_anc1, max_anc1 = lst_ancestors[idx_a][idx_b]
        idx_anc2, min_anc2, max_anc2 = lst_ancestors[idx_anc1][idx_b]
        if idx_anc2 != -1:
            lst_ancestors[idx_a].append([idx_anc2, min(min_anc1, min_anc2), max(max_anc1, max_anc2)])
        else:
            lst_ancestors[idx_a].append([-1, 1000000, 0])

for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    if lst_depth[idx_a] > lst_depth[idx_b]:
        idx_a, idx_b = idx_b, idx_a
    min_ = 1000000
    max_ = 0
    for cnt_ in range(ancestors_max - 1, -1, -1):
        temp_ = lst_depth[idx_b] - lst_depth[idx_a]
        if not temp_:
            break
        elif temp_ >= 2 ** cnt_:
            idx_anc, min_anc, max_anc = lst_ancestors[idx_b][cnt_]
            idx_b = idx_anc
            min_ = min(min_, min_anc)
            max_ = max(max_, max_anc)
    if idx_a != idx_b:
        for cnt_ in range(ancestors_max - 1, -1, -1):
            idx_anc_a, min_anc_a, max_anc_a = lst_ancestors[idx_a][cnt_]
            idx_anc_b, min_anc_b, max_anc_b = lst_ancestors[idx_b][cnt_]
            if idx_anc_a != -1 and idx_anc_a != idx_anc_b:
                idx_a = idx_anc_a
                idx_b = idx_anc_b
                min_ = min(min_, min_anc_a, min_anc_b)
                max_ = max(max_, max_anc_a, max_anc_b)
        min_ = min(min_, lst_ancestors[idx_a][0][1], lst_ancestors[idx_b][0][1])
        max_ = max(max_, lst_ancestors[idx_a][0][2], lst_ancestors[idx_b][0][2])
    print(min_, max_)

exit()
