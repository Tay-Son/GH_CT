import sys

R_, C_ = map(int, sys.stdin.readline().split())
lst_p = [idx_ for idx_ in range(R_ * C_)]
lst_aux = [(-1, 0), (1, 0), (0, -1), (0, 1)]
grd_ = []
for _ in range(R_):
    grd_.append([0 if each_ == 'U' else 1 if each_ == 'D' else 2 if each_ == 'L' else 3 for each_ in
                 sys.stdin.readline().rstrip()])


def id_(idx_r, idx_c):
    return idx_r * C_ + idx_c


def find(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find(temp_)
        lst_p[idx_] = temp_
    return temp_


def union(idx_a, idx_b):
    p_a, p_b = find(idx_a), find(idx_b)
    lst_p[p_b] = p_a


tot_ = 0
grd_iv = [[False for _ in range(C_)] for _ in range(R_)]
for idx_r in range(R_):
    for idx_c in range(C_):
        if not grd_iv[idx_r][idx_c]:
            idx_ = id_(idx_r, idx_c)

            grd_iv[idx_r][idx_c] = True
            offset_r, offset_c = lst_aux[grd_[idx_r][idx_c]]
            t_r = idx_r + offset_r
            t_c = idx_c + offset_c
            idx_t = id_(t_r, t_c)

            while not grd_iv[idx_r][idx_c]:
                grd_iv[idx_r][idx_c] = True
                lst_p[idx_t] = idx_
                idx_r = t_r
                idx_c = t_c

                offset_r, offset_c = lst_aux[grd_[idx_r][idx_c]]
                t_r = idx_r + offset_r
                t_c = idx_c + offset_c
                idx_t = id_(t_r, t_c)

            if find(idx_) != find(idx_t):
                union(idx_, idx_t)
            else:
                tot_ += 1

print(tot_)

exit()
