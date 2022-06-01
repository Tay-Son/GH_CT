import sys
from itertools import combinations as cb

N_ = int(sys.stdin.readline())
lst_ = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
lst_ans = []


def rec_(depth_):
    global lst_
    if depth_ == 3:
        for idx_, val_ in enumerate(lst_):
            if idx_ != val_:
                return False
        else:
            return True
    else:
        if rec_(depth_ + 1):
            lst_ans.append((1, 1))
            return True
        else:
            lst_p = [0]
            for idx_ in range(1, N_):
                val_a, val_b = lst_[idx_ - 1], lst_[idx_]
                if abs(val_a - val_b) != 1:
                    if idx_ - lst_p[-1] == 2:
                        lst_p.append(idx_ - 1)
                    lst_p.append(idx_)
            lst_p.append(N_)

            for ptr_l, ptr_r in cb(lst_p, 2):
                lst_ = lst_[:ptr_l] + [val_ for val_ in reversed(lst_[ptr_l:ptr_r])] + lst_[ptr_r:]
                if rec_(depth_ + 1):
                    lst_ans.append((ptr_l + 1, ptr_r))
                    return True
                lst_ = lst_[:ptr_l] + [val_ for val_ in reversed(lst_[ptr_l:ptr_r])] + lst_[ptr_r:]
            else:
                return False


rec_(0)

for ptr_l, ptr_r in reversed(lst_ans):
    print(ptr_l, ptr_r)

exit()
