import sys
sys.setrecursionlimit(2509)

lst_aux = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def rec_(grd_, idx_m, idx_n):
    grd_[idx_n][idx_m] = False
    M_ = len(grd_[0])
    N_ = len(grd_)
    for off_m, off_n in lst_aux:
        idx_target_m = idx_m + off_m
        idx_target_n = idx_n + off_n
        if 0 <= idx_target_m < M_ and 0 <= idx_target_n < N_ and grd_[idx_target_n][idx_target_m]:
            rec_(grd_, idx_target_m, idx_target_n)


for _ in range(int(sys.stdin.readline())):
    M_, N_, K_ = map(int, sys.stdin.readline().split())
    grd_ = [[False for _ in range(M_)] for _ in range(N_)]

    lst_ = []
    for _ in range(K_):
        val_a, val_b = map(int, sys.stdin.readline().split())
        grd_[val_b][val_a] = True
        lst_.append([val_a, val_b])

    tot_ = 0
    for idx_m, idx_n in lst_:
        if grd_[idx_n][idx_m]:
            tot_ += 1
            rec_(grd_, idx_m, idx_n)

    print(tot_)

exit()