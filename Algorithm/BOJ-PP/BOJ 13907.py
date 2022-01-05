import sys
import heapq as hq

INF_ = 1000000009

N_, M_, K_ = map(int, sys.stdin.readline().split())
S_, D_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    idx_a, idx_b, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_a].append((idx_b, weight_))
    grp_[idx_b].append((idx_a, weight_))

lst_dist = [[INF_ for _ in range(N_ + 1)] for _ in range(N_ + 1)]
lst_dist[S_][0] = (0, 0)
lst_iv = [[False for _ in range(N_ + 1)] for _ in range(N_ + 1)]

hqu_ = [(0, 0, S_)]
while hqu_:
    depth_, dist_, idx_s = hq.heappop(hqu_)
    if not lst_iv[idx_s][depth_]:
        lst_iv[idx_s][depth_] = True
        depth_ += 1
        for idx_e, weight_ in grp_[idx_s]:
            print(idx_e, weight_)
            temp_ = dist_ + weight_
            if temp_ < lst_dist[idx_e][depth_]:
                lst_dist[idx_e][depth_] = temp_
                hq.heappush(hqu_, (depth_, temp_, idx_e))

for _ in range(K_):
    pass

print(lst_dist[D_])

exit()
