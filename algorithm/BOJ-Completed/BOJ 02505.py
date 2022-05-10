import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
lst_d = [val_ for val_ in lst_]

ptr_l = 0
lst_ans = []
for _ in range(2):
    while ptr_l < N_ - 1 and lst_[ptr_l] == ptr_l:
        ptr_l += 1
    # ptr_r = ptr_l + 1
    ptr_r = ptr_l
    while ptr_r < N_ - 1 and lst_[ptr_r] != ptr_l:
        ptr_r += 1
    lst_ = lst_[:ptr_l] + [val_ for val_ in reversed(lst_[ptr_l:ptr_r + 1])] + lst_[ptr_r + 1:]
    lst_ans.append((ptr_l + 1, ptr_r + 1))

for idx_, val_ in enumerate(lst_):
    if idx_ != val_:
        ptr_r = N_ - 1
        lst_ans = []
        for _ in range(2):
            while 0 < ptr_r and lst_d[ptr_r] == ptr_r:
                ptr_r -= 1
            # ptr_l = ptr_r - 1
            ptr_l = ptr_r
            while 0 < ptr_l and lst_d[ptr_l] != ptr_r:
                ptr_l -= 1
            # ptr_r += 1
            lst_d = lst_d[:ptr_l] + [val_ for val_ in reversed(lst_d[ptr_l:ptr_r + 1])] + lst_d[ptr_r + 1:]
            lst_ans.append((ptr_l + 1, ptr_r + 1))
        break

for each_ in lst_ans:
    print(' '.join(map(str, each_)))

exit()
