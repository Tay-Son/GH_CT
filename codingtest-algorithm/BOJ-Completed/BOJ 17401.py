import sys

DIV_ = 1000000007


def mat_mult(mat_a, mat_b):
    A_, B_, C_ = len(mat_a), len(mat_a[0]), len(mat_b[0])

    mat_o = [[0 for _ in range(C_)] for _ in range(A_)]
    for idx_a in range(A_):
        for idx_c in range(C_):
            tot_ = 0
            for idx_b in range(B_):
                tot_ += mat_a[idx_a][idx_b] * mat_b[idx_b][idx_c]
                tot_ %= DIV_
            mat_o[idx_a][idx_c] = tot_

    return mat_o


def mat_pow(mat_, num_):
    R_, C_ = len(mat_), len(mat_[0])

    mat_o = [[0 for _ in range(R_)] for _ in range(R_)]
    for idx_ in range(R_):
        mat_o[idx_][idx_] = 1
    while num_:
        num_, is_ = divmod(num_, 2)

        if is_:
            mat_o = mat_mult(mat_o, mat_)

        mat_ = mat_mult(mat_, mat_)
    return mat_o


T_, N_, D_ = map(int, sys.stdin.readline().split())

lst_mat = [[[0 for _ in range(N_)] for _ in range(N_)] for _ in range(T_)]

for idx_t in range(T_):
    for _ in range(int(sys.stdin.readline())):
        idx_a, idx_b, num_ = map(int, sys.stdin.readline().split())
        idx_a, idx_b = idx_a - 1, idx_b - 1
        lst_mat[idx_t][idx_a][idx_b] = num_

num_, D_ = divmod(D_, T_)

if not num_:
    mat_ = [[0 for _ in range(N_)] for _ in range(N_)]
    for idx_ in range(N_):
        mat_[idx_][idx_] = 1

    for each_mat in lst_mat[:D_]:
        mat_ = mat_mult(mat_, each_mat)


else:
    mat_ = [[0 for _ in range(N_)] for _ in range(N_)]
    for idx_ in range(N_):
        mat_[idx_][idx_] = 1

    for idx_, each_mat in enumerate(lst_mat):
        mat_ = mat_mult(mat_, each_mat)
        if idx_ == D_ - 1:
            mat_temp = mat_.copy()

    mat_ = mat_pow(mat_, num_)
    if D_:
        mat_ = mat_mult(mat_, mat_temp)

for each_ in mat_:
    print(' '.join(map(str, each_)))

exit()
