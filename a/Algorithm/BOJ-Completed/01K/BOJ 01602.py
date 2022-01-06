import sys

INF_ = 5000000

N_, M_, Q_ = map(int, sys.stdin.readline().split())
lst_b = [0] + list(map(int, sys.stdin.readline().split()))

mat_ = [[[INF_, max(lst_b[idx_s], lst_b[idx_e])] for idx_e in range(N_ + 1)] for idx_s in range(N_ + 1)]
lst_b = sorted(list(zip(lst_b, range(N_ + 1))), key=lambda x: x[0])
for idx_ in range(1, N_ + 1):
    mat_[idx_][idx_][0] = 0
    mat_[idx_][idx_][1] = 0

for _ in range(M_):
    S_, E_, W_ = map(int, sys.stdin.readline().split())
    mat_[S_][E_][0] = W_
    mat_[E_][S_][0] = W_

for each_ in lst_b[1:]:
    idx_m = each_[1]
    for idx_s in range(1, N_ + 1):
        for idx_e in range(1, N_ + 1):
            temp_a = mat_[idx_s][idx_m][0] + mat_[idx_m][idx_e][0]
            if mat_[idx_s][idx_m][1] >= mat_[idx_m][idx_e][1]:
                temp_b = mat_[idx_s][idx_m][1]
            else:
                temp_b = mat_[idx_m][idx_e][1]
            if temp_a + temp_b < mat_[idx_s][idx_e][0] + mat_[idx_s][idx_e][1]:
                mat_[idx_s][idx_e][0] = temp_a
                mat_[idx_s][idx_e][1] = temp_b

for idx_s in range(1, N_ + 1):
    for idx_e in range(1, N_ + 1):
        if mat_[idx_s][idx_e][0] == INF_:
            mat_[idx_s][idx_e][0] = -1
        else:
            mat_[idx_s][idx_e][0] += mat_[idx_s][idx_e][1]

for _ in range(Q_):
    S_, T_ = map(int, sys.stdin.readline().split())
    print(mat_[S_][T_][0])

exit()
