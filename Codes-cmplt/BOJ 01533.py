import sys

DIV_ = 1000003

N_, S_, E_, T_ = map(int, sys.stdin.readline().split())


def mat_mult(mat_a, mat_b):
    mat_out = [[0 for _ in range(N_ * 5 + 1)] for _ in range(N_ * 5 + 1)]
    for idx_a in range(1, N_ * 5 + 1):
        for idx_b in range(1, N_ * 5 + 1):
            for idx_c in range(1, N_ * 5 + 1):
                mat_out[idx_a][idx_b] += mat_a[idx_a][idx_c] * mat_b[idx_c][idx_b]
                mat_out[idx_a][idx_b] %= DIV_
    return mat_out


mat_ = [[0 for _ in range(N_ * 5 + 1)] for _ in range(N_ * 5 + 1)]
for idx_a in range(1, N_ + 1):
    lst_input = sys.stdin.readline().rstrip()
    for idx_b in range(N_):
        temp_ = int(lst_input[idx_b])
        if temp_ > 0:
            mat_[idx_a * 5][(idx_b + 1) * 5 - (temp_ - 1)] = 1
    for idx_b in range(1, 5):
        mat_[(idx_a - 1) * 5 + idx_b][(idx_a - 1) * 5 + idx_b + 1] = 1

mat_dp = [[0 for _ in range(N_ * 5 + 1)] for _ in range(N_ * 5 + 1)]
for idx_ in range(1, N_ * 5 + 1):
    mat_dp[idx_][idx_] = 1
while T_:
    T_, mod_ = divmod(T_, 2)
    if mod_:
        mat_dp = mat_mult(mat_dp, mat_)
    mat_ = mat_mult(mat_, mat_)

print(mat_dp[S_ * 5][E_ * 5])

for each_ in mat_dp:
    print(each_)
print()

exit()
