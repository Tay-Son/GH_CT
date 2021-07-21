import sys
import heapq as hq

INF_ = 10 ** 9


def dijk_(grp_, S_):
    lst_distance = [INF_ for _ in range(len(grp_))]
    lst_distance[S_] = 0
    lst_is_visited = [False for _ in range(len(grp_))]
    hqu_ = [(0, S_)]

    while hqu_:
        distance_, idx_s = hq.heappop(hqu_)
        if not lst_is_visited[idx_s]:
            lst_is_visited[idx_s] = True
            for idx_e, weight_ in grp_[idx_s]:
                temp_ = distance_ + weight_
                if temp_ < lst_distance[idx_e]:
                    lst_distance[idx_e] = temp_
                    hq.heappush(hqu_, (temp_, idx_e))
    return lst_distance


N_, E_ = map(int, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_ + 1)]

for _ in range(E_):
    idx_s, idx_e, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_s].append((idx_e, weight_))
    grp_[idx_e].append((idx_s, weight_))

V1_, V2_ = map(int, sys.stdin.readline().split())

lst_d_s = dijk_(grp_, 1)
lst_d_v1 = dijk_(grp_, V1_)
lst_d_v2 = dijk_(grp_, V2_)

answer_ = min(lst_d_s[V1_] + lst_d_v1[V2_] + lst_d_v2[N_],
              lst_d_s[V2_] + lst_d_v2[V1_] + lst_d_v1[N_])
if answer_ < INF_:
    print(answer_)
else:
    print(-1)

exit()
