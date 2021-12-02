import sys
import heapq as hq

INF_ = 1000000007

N_, M_, K_ = map(int, sys.stdin.readline().split())
S_, D_ = map(lambda x: int(x) - 1, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_)]
for _ in range(M_):
    a_, b_, dist_ = map(int, sys.stdin.readline().split())
    a_, b_ = a_ - 1, b_ - 1
    grp_[a_].append((b_, dist_))
    grp_[b_].append((a_, dist_))

grd_dist = [[INF_ for _ in range(N_)] for _ in range(N_)]
grd_dist[S_][0] = 0
hqu_ = [(0, 0, S_)]

while hqu_:
    tot_dist, tot_mov, idx_s = hq.heappop(hqu_)
    if idx_s != D_:
        for mov_ in range(tot_mov):
            if grd_dist[idx_s][mov_] < tot_dist:
                break
        else:
            tot_mov += 1
            if tot_mov < N_:
                for idx_e, dist_ in grp_[idx_s]:
                    temp_ = tot_dist + dist_
                    if temp_ < grd_dist[idx_e][tot_mov]:
                        grd_dist[idx_e][tot_mov] = temp_
                        hq.heappush(hqu_, (temp_, tot_mov, idx_e))

lst_ = []
for idx_, val_ in enumerate(grd_dist[D_]):
    if val_ != INF_:
        lst_.append((val_, idx_))

tot_ = 0
print(min([idx_ * tot_ + val_ for val_, idx_ in lst_]))
for _ in range(K_):
    tot_ += int(sys.stdin.readline())
    print(min([idx_ * tot_ + val_ for val_, idx_ in lst_]))

exit()
