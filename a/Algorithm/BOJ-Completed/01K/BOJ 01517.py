import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

tot_ = 0


def rec_(idx_s, idx_e):
    global tot_
    if idx_s + 1 < idx_e:
        idx_c = (idx_s + idx_e) // 2
        lst_l = rec_(idx_s, idx_c)
        lst_r = rec_(idx_c, idx_e)

        lst_temp = []
        ptr_r = 0
        for ptr_l in range(len(lst_l)):
            while ptr_r < len(lst_r) and lst_l[ptr_l] > lst_r[ptr_r]:
                lst_temp.append(lst_r[ptr_r])
                ptr_r += 1
                tot_ += len(lst_l) - ptr_l
            lst_temp.append(lst_l[ptr_l])
        while ptr_r < len(lst_r):
            lst_temp.append(lst_r[ptr_r])
            ptr_r += 1
        return lst_temp
    else:
        return [lst_[idx_s]]


rec_(0, N_)
print(tot_)

exit()
