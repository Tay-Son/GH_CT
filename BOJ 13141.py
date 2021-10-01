import sys

INF_ = 1000000009

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = []
mat_dist = [[INF_ for _ in range(N_)] for _ in range(N_)]

for _ in range(M_):
    idx_a, idx_b, dist_ = map(int, sys.stdin.readline().split())
    idx_a, idx_b = idx_a - 1, idx_b - 1
    if idx_a == idx_b:
        grp_[idx_a].append((-1, dist_))
        grp_[idx_b].append((-1, dist_))
        pass
    else:
        mat_dist[idx_a][idx_b] = min(dist_, mat_dist[idx_a][idx_b])
        mat_dist[idx_b][idx_a] = min(dist_, mat_dist[idx_b][idx_a])
        grp_[idx_a].append((idx_b, dist_))
        grp_[idx_b].append((idx_a, dist_))

for idx_m in range(N_):
    mat_dist[idx_m][idx_m] = 0
    for idx_s in range(N_):
        for idx_e in range(N_):
            temp_ = mat_dist[idx_s][idx_m] + mat_dist[idx_m][idx_e]
            if temp_ < mat_dist[idx_s][idx_e]:
                mat_dist[idx_s][idx_e] = temp_

min_ = INF_
for idx_, dist_max in sorted([(idx_, max(mat_dist[idx_])) for idx_ in range(N_)], key=lambda x: x[1]):
    if dist_max >= min_:
        break
    else:
        lst_iv = [-1 for _ in range(N_)]
        lst_iv[idx_] = 0

        max_ = 0
        que_ = [(0, idx_)]
        idx_que = 0
        while idx_que < len(que_):



print(min_)

exit()
