import sys
import heapq

N_ = int(sys.stdin.readline())
grd_ = []
for _ in range(N_):
    grd_.append(list(map(int, sys.stdin.readline().split())))
lst_ptr = [N_ - 1 for _ in range(N_)]

que_ = []
for idx_ in range(N_):
    heapq.heappush(que_, (-grd_[-1][idx_], idx_))
for _ in range(N_):
    curr_, lane_ = heapq.heappop(que_)
    lst_ptr[lane_] -= 1
    heapq.heappush(que_, (-grd_[lst_ptr[lane_]][lane_], lane_))
print(-curr_)

exit()