import sys
import heapq as hq

INF_ = 10000

M_, N_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N_):
    lst_temp = list(map(int, list(sys.stdin.readline().rstrip())))
    grd_.append(lst_temp)

lst_distance = [[INF_ for _ in range(M_)] for _ in range(N_)]
lst_distance[0][0] = 0
que_distance = [(0, 0, 0)]

while que_distance:
    curr_w, curr_n, curr_m = hq.heappop(que_distance)
    if curr_n != N_ - 1:
        temp_ = curr_w + grd_[curr_n + 1][curr_m]
        if temp_ < lst_distance[curr_n + 1][curr_m]:
            lst_distance[curr_n + 1][curr_m] = temp_
            hq.heappush(que_distance, (temp_, curr_n + 1, curr_m))
    if curr_n != 0:
        temp_ = curr_w + grd_[curr_n - 1][curr_m]
        if temp_ < lst_distance[curr_n - 1][curr_m]:
            lst_distance[curr_n - 1][curr_m] = temp_
            hq.heappush(que_distance, (temp_, curr_n - 1, curr_m))
    if curr_m != M_ - 1:
        temp_ = curr_w + grd_[curr_n][curr_m + 1]
        if temp_ < lst_distance[curr_n][curr_m + 1]:
            lst_distance[curr_n][curr_m + 1] = temp_
            hq.heappush(que_distance, (temp_, curr_n, curr_m + 1))
    if curr_m != 0:
        temp_ = curr_w + grd_[curr_n][curr_m - 1]
        if temp_ < lst_distance[curr_n][curr_m - 1]:
            lst_distance[curr_n][curr_m - 1] = temp_
            hq.heappush(que_distance, (temp_, curr_n, curr_m - 1))

print(lst_distance[N_ - 1][M_ - 1])

exit()