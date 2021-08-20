import sys

N_, K_ = map(int, sys.stdin.readline().split())

dct_ = dict()
ptr_s = 0
count_ = 0
count_max = count_

lst_ = list(map(int, sys.stdin.readline().split()))
for each_ in lst_:
    if each_ not in dct_:
        dct_[each_] = 1
        count_ += 1
        count_max = max(count_max, count_)
    else:
        dct_[each_] += 1
        count_ += 1
        while dct_[each_] > K_:
            val_ = lst_[ptr_s]
            ptr_s += 1
            dct_[val_] -= 1
            count_ -= 1

        count_max = max(count_max, count_)
print(count_max)

exit()