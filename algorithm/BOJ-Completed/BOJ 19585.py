import sys

lst_tmp = [0 for _ in range(27)]

C_, N_ = map(int, sys.stdin.readline().split())

tri_ = [lst_tmp.copy()]
set_ = set()


def add_(str_):
    idx_tri = 0
    for chr_ in str_:
        idx_ = ord(chr_) - ord('a') + 1
        if not tri_[idx_tri][idx_]:
            tri_[idx_tri][idx_] = len(tri_)
            tri_.append(lst_tmp.copy())
        idx_tri = tri_[idx_tri][idx_]
    tri_[idx_tri][0] = 1


def search_(str_):
    is_ = False
    idx_tri = 0

    for ptr_str in range(len(str_)):
        chr_ = str_[ptr_str]
        idx_ = ord(chr_) - ord('a') + 1
        temp_ = tri_[idx_tri][idx_]
        if not temp_:
            break
        else:
            idx_tri = temp_
            if tri_[idx_tri][0] and str_[ptr_str + 1:] in set_:
                is_ = True
                break

    return is_


for _ in range(C_):
    add_(sys.stdin.readline().rstrip())
for _ in range(N_):
    set_.add(sys.stdin.readline().rstrip())
for _ in range(int(sys.stdin.readline())):
    if search_(sys.stdin.readline().rstrip()):
        print('Yes')
    else:
        print('No')

exit()
