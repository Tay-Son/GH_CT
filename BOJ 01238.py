import sys
import heapq as hq

INF_ = 10 ** 9

N_, M_, X_ = map(int, sys.stdin.readline().split())

lst_grp = [[[] for _ in range(N_ + 1)] for _ in range(2)]
grd_distance = [[INF_ for _ in range(N_ + 1)] for _ in range(2)]
lst_hqu = [[(0, X_)], [(0, X_)]]
grd_is_visited = [[False for _ in range(N_ + 1)] for _ in range(2)]
grd_distance[0][X_] = 0
grd_distance[1][X_] = 0

for _ in range(M_):
    idx_s, idx_e, weight_ = map(int, sys.stdin.readline().split())
    lst_grp[0][idx_s].append((idx_e, weight_))
    lst_grp[1][idx_e].append((idx_s, weight_))

for cnt_ in range(2):
    while lst_hqu[cnt_]:
        distance_, idx_s = hq.heappop(lst_hqu[cnt_])
        if not grd_is_visited[cnt_][idx_s]:
            grd_is_visited[cnt_][idx_s] = True
            for idx_e, weight_ in lst_grp[cnt_][idx_s]:
                temp_ = distance_ + weight_
                if temp_ < grd_distance[cnt_][idx_e]:
                    grd_distance[cnt_][idx_e] = temp_
                    hq.heappush(lst_hqu[cnt_], (temp_, idx_e))

print(max([grd_distance[0][idx_] + grd_distance[1][idx_] for idx_ in range(1, N_ + 1)]))
exit()
