import sys
import heapq as hq

INF_ = 10 ** 9

N_ = int(sys.stdin.readline())
lst_distance = [INF_ for _ in range(N_ + 1)]
lst_is_visited = [False for _ in range(N_ + 1)]
grp_ = [[] for _ in range(N_ + 1)]

for _ in range(int(sys.stdin.readline())):
    idx_s, idx_e, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_s].append((idx_e, weight_))

S_, E_ = map(int, sys.stdin.readline().split())
lst_distance[S_] = 0
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

print(lst_distance[E_])

exit()
