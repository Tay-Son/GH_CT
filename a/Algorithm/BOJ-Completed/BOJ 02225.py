import sys

DIV_ = 1000000000
N_, K_ = map(int, sys.stdin.readline().split())
grd_ = [[0 for _ in range(201)] for _ in range(201)]
for idx_ in range(201):
    grd_[idx_][1] = 1
for idx_ in range(1, 201):
    for idx_b in range(201):
        for idx_c in range(idx_b + 1):
            grd_[idx_b][idx_] += grd_[idx_c][idx_ - 1]
print(grd_[N_][K_] % DIV_)
exit()
