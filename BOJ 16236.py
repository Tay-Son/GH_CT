import sys
import heapq as hq

N_ = int(sys.stdin.readline())
grd_ = []
for idx_r in range(N_):
    lst_temp = list(map(int, sys.stdin.readline().split()))
    for idx_c, value_ in enumerate(lst_temp):
        if value_ == 9:
            c_r, c_c = idx_r, idx_c
            lst_temp[idx_c] = 0
    grd_.append(lst_temp)

for each_ in grd_:
    print(each_)
print()

tot_ = 0
size_ = 2
is_run = True
while is_run:
    grd_iv = [[False for _ in range(N_)] for _ in range(N_)]
    lst_ = []

    hqu_ = [(0, c_r, c_c)]
    while hqu_:
        depth_, e_r, e_c = hq.heappop(hqu_)
        if not grd_iv[e_r][e_c]:
            grd_iv[e_r][e_c] = True
            if 0 < grd_[e_r][e_c] < size_:
                lst_.append((grd_[e_r][e_c], depth_, e_r, e_c))
            depth_ += 1
            for o_r, o_c in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                t_r, t_c = e_r + o_r, e_c + o_c
                if 0 <= t_r < N_ and 0 <= t_c < N_ and grd_[t_r][t_c] <= size_:
                    hq.heappush(hqu_, (depth_, t_r, t_c))

    lst_.sort(key=lambda x: x[1])
    lst_.sort(key=lambda x: x[0])

    if lst_:
        c_r, c_c = lst_[0][2], lst_[0][3]
        grd_[c_r][c_c] = 0
        tot_ += lst_[0][1]
        size_ += 1
    else:
        is_run = False

print(tot_)

exit()
