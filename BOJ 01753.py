import sys
import heapq as hq

INF_ = 10 ** 9

V_, E_ = map(int, sys.stdin.readline().split())
lst_distance = [INF_ for _ in range(V_ + 1)]

hqu_ = []
S_ = int(sys.stdin.readline())
lst_distance[S_] = 0
hq.heappush(hqu_, (0, S_))

grp_ = [[] for _ in range(V_ + 1)]

for _ in range(E_):
    idx_s, idx_e, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_s].append((idx_e, weight_))

lst_is_visited = [False for _ in range(V_ + 1)]
while hqu_:
    dist_, idx_s = hq.heappop(hqu_)
    if not lst_is_visited[idx_s]:
        lst_is_visited[idx_s] = True
        for idx_e, weight_ in grp_[idx_s]:
            temp_ = dist_ + weight_

            if temp_ < lst_distance[idx_e]:
                lst_distance[idx_e] = temp_
                hq.heappush(hqu_, (temp_, idx_e))

for idx_ in range(1, V_ + 1):
    temp_ = lst_distance[idx_]
    if temp_ == INF_:
        print('INF')
    else:
        print(temp_)

exit()