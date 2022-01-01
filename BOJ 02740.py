import sys


def mat_mult(mat_a, mat_b):
    N_, M_, K_ = len(mat_a), len(mat_a[0]), len(mat_b[0])

    mat_ = []
    for idx_n in range(N_):
        lst_ = []
        for idx_k in range(K_):
            tot_ = 0
            for idx_m in range(M_):
                tot_ += mat_a[idx_n][idx_m] * mat_b[idx_m][idx_k]
            lst_.append(tot_)
        mat_.append(lst_)
    return mat_


N_, M_ = map(int, sys.stdin.readline().split())
mat_a = []
for _ in range(N_):
    mat_a.append(list(map(int, sys.stdin.readline().split())))

M_, K_ = map(int, sys.stdin.readline().split())
mat_b = []
for _ in range(M_):
    mat_b.append(list(map(int, sys.stdin.readline().split())))

mat_ = mat_mult(mat_a, mat_b)
for each_ in mat_:
    print(' '.join(map(str, each_)))

exit()
