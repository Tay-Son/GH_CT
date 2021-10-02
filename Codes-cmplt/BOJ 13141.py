import sys
import heapq as hq

INF_ = 1000000009

N_, M_ = map(int, sys.stdin.readline().split())
grp_ = [[] for _ in range(N_)]
mat_dist = [[INF_ for _ in range(N_)] for _ in range(N_)]

for _ in range(M_):
    idx_a, idx_b, dist_ = map(int, sys.stdin.readline().split())
    idx_a, idx_b = idx_a - 1, idx_b - 1
    if idx_a == idx_b:
        grp_[idx_a].append((idx_b, dist_))
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
idx_, dist_max = sorted([(idx_, max(mat_dist[idx_])) for idx_ in range(N_)], key=lambda x: x[1])[0]
lst_iv = [-1 for _ in range(N_)]
max_ = 0.0
hqu_ = [(0, idx_)]
while hqu_:
    time_, idx_s = hq.heappop(hqu_)
    if lst_iv[idx_s] == -1:
        max_ = max(max_, time_)
        lst_iv[idx_s] = time_
        for idx_e, dist_ in grp_[idx_s]:
            if lst_iv[idx_e] == -1:
                hq.heappush(hqu_, (dist_ + time_, idx_e))
            elif lst_iv[idx_e] > time_ - dist_:
                max_ = max(max_, (lst_iv[idx_e] + time_ + dist_) / 2)
min_ = min(min_, max_)

print(float(min_))

exit()
