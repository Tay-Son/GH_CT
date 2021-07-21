import sys

INF_ = 10 ** 9

N_, M_ = map(int, sys.stdin.readline().split())
mat_ = [[INF_ for _ in range(N_)] for _ in range(N_)]

for _ in range(M_):
    idx_a, idx_b = map(int, sys.stdin.readline().split())
    idx_a -= 1
    idx_b -= 1
    mat_[idx_a][idx_b] = 1
    mat_[idx_b][idx_a] = 1

for idx_via in range(N_):
    for idx_s in range(N_):
        for idx_e in range(N_):
            mat_[idx_s][idx_e] = min(mat_[idx_s][idx_e], mat_[idx_s][idx_via] + mat_[idx_via][idx_e])

min_ = INF_
idx_min = 0
for idx_s in range(N_):
    temp_ = sum(mat_[idx_s])
    if temp_ < min_:
        min_ = temp_
        idx_min = idx_s

print(idx_min + 1)

exit()
