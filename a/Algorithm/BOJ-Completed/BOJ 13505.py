import sys
import math


def add(tri_, val_, len_max):
    lst_val = list(map(int, str(bin(val_))[2:].zfill(len_max)))
    idx_curr = 0

    for each_ in lst_val[:-1]:
        if tri_[idx_curr][each_] == -1:
            tri_[idx_curr][each_] = len(tri_)
            tri_.append([-1, -1])
        idx_curr = tri_[idx_curr][each_]
    tri_[idx_curr][lst_val[-1]] = len(tri_)


def find(tri_, val_, len_max):
    lst_val = list(map(int, str(bin(val_))[2:].zfill(len_max)))

    idx_curr = 0
    val_curr = 2 ** (len_max - 1)
    tot_ = 0

    for each_ in lst_val:
        temp_ = tri_[idx_curr][not each_]
        if temp_ != -1:
            tot_ += val_curr
            idx_curr = temp_
        else:
            idx_curr = tri_[idx_curr][each_]
        val_curr //= 2

    return tot_


N_ = int(sys.stdin.readline())

lst_ = list(map(int, sys.stdin.readline().split()))
len_max = math.ceil(math.log2(max(lst_))) + 1
tri_ = [[-1, -1]]
for each_ in lst_:
    add(tri_, each_, len_max)

max_ = 0
for each_ in lst_:
    max_ = max(max_, find(tri_, each_, len_max))
print(max_)

exit()
