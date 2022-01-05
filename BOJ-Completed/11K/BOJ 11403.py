import sys

N_ = int(sys.stdin.readline())

mat_ = []
for _ in range(N_):
    mat_.append(list(map(int, sys.stdin.readline().split())))

for idx_via in range(N_):
    for idx_s in range(N_):
        for idx_e in range(N_):
            if mat_[idx_s][idx_via] + mat_[idx_via][idx_e] == 2:
                mat_[idx_s][idx_e] = 1

for each_ in mat_:
    print(' '.join(map(str, each_)))
exit()
