import sys
import heapq as hq


def find_(lst_p, idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(lst_p, temp_)
        lst_p[idx_] = temp_
    return temp_


def union(lst_p, idx_a, idx_b):
    p_a, p_b = find_(lst_p, idx_a), find_(lst_p, idx_b)
    lst_p[p_a] = p_b


N_, M_ = map(int, sys.stdin.readline().split())
lst_p = [idx_ for idx_ in range(N_ + 1)]
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(M_):
    A_, B_, C_ = map(int, sys.stdin.readline().split())
    grp_[A_].append((B_, C_))
    grp_[B_].append((A_, C_))

S_, E_ = map(int, sys.stdin.readline().split())

min_ = 1000000000
hqu_ = []
idx_curr = S_
for idx_target, weight_ in grp_[S_]:
    hq.heappush(hqu_, (-weight_, idx_target))

while find_(lst_p, S_) != find_(lst_p, E_):
    weight_, idx_curr = hq.heappop(hqu_)
    if find_(lst_p, idx_curr) != find_(lst_p, S_):
        union(lst_p, idx_curr, S_)
        min_ = min(min_, -weight_)
        for idx_target, weight_ in grp_[idx_curr]:
            hq.heappush(hqu_, (-weight_, idx_target))

print(min_)

exit()
