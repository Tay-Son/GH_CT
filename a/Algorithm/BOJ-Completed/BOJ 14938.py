import sys

INF_ = 1000000007

N_, M_, R_ = map(int, sys.stdin.readline().split())
lst_t = list(map(int, sys.stdin.readline().split()))

mat_ = [[INF_ if idx_s != idx_e else 0 for idx_e in range(N_)] for idx_s in range(N_)]
for _ in range(R_):
    a_, b_, w_ = map(int, sys.stdin.readline().split())
    a_ -= 1
    b_ -= 1
    mat_[a_][b_] = w_
    mat_[b_][a_] = w_

for idx_w in range(N_):
    for idx_s in range(N_):
        for idx_e in range(N_):
            mat_[idx_s][idx_e] = min(mat_[idx_s][idx_e], mat_[idx_s][idx_w] + mat_[idx_w][idx_e])

max_ = 0
for idx_s in range(N_):
    tot_ = 0
    for idx_e in range(N_):
        if mat_[idx_s][idx_e] <= M_:
            tot_ += lst_t[idx_e]
    max_ = max(max_, tot_)

for each_ in mat_:
    print(each_)

print(max_)

exit()
