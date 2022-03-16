import sys

INF_ = 10 ** 9

N_ = int(sys.stdin.readline())

mat_ = [[INF_ for _ in range(N_)] for _ in range(N_)]

for idx_ in range(N_):
    mat_[idx_][idx_] = 0

for _ in range(int(sys.stdin.readline())):
    idx_a, idx_b, cost_ = map(int, sys.stdin.readline().split())
    idx_a -= 1
    idx_b -= 1
    mat_[idx_a][idx_b] = min(mat_[idx_a][idx_b], cost_)

for idx_via in range(N_):
    for idx_s in range(N_):
        for idx_e in range(N_):
            mat_[idx_s][idx_e] = min(mat_[idx_s][idx_e],
                                     mat_[idx_s][idx_via] + mat_[idx_via][idx_e])

for idx_s in range(N_):
    for idx_e in range(N_):
        if mat_[idx_s][idx_e] >= INF_:
            mat_[idx_s][idx_e] = 0

for each_ in mat_:
    print(' '.join(map(str, each_)))

exit()
