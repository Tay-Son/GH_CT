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