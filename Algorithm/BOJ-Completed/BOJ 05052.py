import sys

lst_tri = list(map(chr, range(10)))
tri_temp = [-1 for _ in range(1 + len(lst_tri))]


def idx(chr_):
    return int(chr_) + 1


def add(tri_, str_):
    idx_curr = 0
    for each_ in str_:
        idx_temp = idx(each_)
        if tri_[idx_curr][idx_temp] == -1:
            tri_[idx_curr][idx_temp] = len(tri_)
            tri_.append(tri_temp.copy())
        idx_curr = tri_[idx_curr][idx_temp]
    tri_[idx_curr][0] = 0


def find_prefix(tri_, str_):

    idx_curr = 0
    is_a = False
    is_b = False
    for each_ in str_[:-1]:
        if tri_[idx_curr][0] == 0:
            is_a = True
            break
        idx_temp = idx(each_)
        temp_ = tri_[idx_curr][idx_temp]
        if temp_ == -1:
            is_b = True
            break
        else:
            idx_curr = temp_

    if not is_b:
        if tri_[idx_curr][0] == 0:
            is_a = True
        else:
            idx_temp = idx(str_[-1])
            temp_ = tri_[idx_curr][idx_temp]
            if temp_ != -1:
                is_a = True
    return is_a


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    N_ = int(sys.stdin.readline())
    lst_input = [sys.stdin.readline().rstrip() for _ in range(N_)]
    is_ = True
    tri_ = [tri_temp.copy()]
    for each_ in lst_input:
        if not find_prefix(tri_, each_):
            add(tri_, each_)
        else:
            is_ = False
            break
    if is_:
        print('YES')
    else:
        print('NO')

exit()