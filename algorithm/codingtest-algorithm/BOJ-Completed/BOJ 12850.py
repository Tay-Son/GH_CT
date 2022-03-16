import sys

DIV_ = 1000000007
mat_i = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]


def mat_mul(mat_a, mat_b):
    len_w = len(mat_a[0])
    len_a = len(mat_a)
    len_b = len(mat_b[0])

    mat_o = []
    for idx_a in range(len_a):
        lst_temp = []
        for idx_b in range(len_b):
            tot_ = 0
            for idx_w in range(len_w):
                tot_ += mat_a[idx_a][idx_w] * mat_b[idx_w][idx_b]
                tot_ %= DIV_
            lst_temp.append(tot_)
        mat_o.append(lst_temp)
    return mat_o


def mat_pow(mat_, count_):
    len_ = len(mat_)
    mat_o = [[1 if idx_c == idx_r else 0 for idx_c in range(len_)] for idx_r in range(len_)]

    while count_:
        count_, is_ = divmod(count_, 2)
        if is_:
            mat_o = mat_mul(mat_o, mat_)
        mat_ = mat_mul(mat_, mat_)
    return mat_o


print(mat_pow(mat_i, int(sys.stdin.readline()))[0][0])

exit()
