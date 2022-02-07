def mat_mul(mat_a, mat_b):
    len_w = len(mat_a[0])
    len_a = len(mat_a)
    len_b = len(mat_b[0])

    mat_o = []
    for idx_a in range(len_a):
        lst_temp = []
        for idx_b in range(len_b):
            is_ = False
            for idx_w in range(len_w):
                if mat_a[idx_a][idx_w] and mat_b[idx_w][idx_b]:
                    is_ = True
                    break
            lst_temp.append(int(is_))
        mat_o.append(lst_temp)
    return mat_o


def mat_add(mat_a, mat_b):
    len_r = len(mat_a)
    len_c = len(mat_a[0])

    mat_o = []

    for idx_r in range(len_r):
        lst_temp = []
        for idx_c in range(len_c):
            lst_temp.append(1 if mat_a[idx_r][idx_c] + mat_b[idx_r][idx_c] else 0)
        mat_o.append(lst_temp)
    return mat_o


def solution(N_, mat_sign):
    mat_ = mat_sign.copy()
    for _ in range(N_ - 1):
        mat_ = mat_add(mat_, mat_mul(mat_, mat_sign))
    return mat_


print(solution(3, [[0, 0, 1], [0, 0, 1], [0, 1, 0]]))
