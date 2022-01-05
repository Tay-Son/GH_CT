import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

M_ = int(sys.stdin.readline())
C_ = 1000
grd_quary = [[] for _ in range(C_)]
lst_quary = []
lst_answer = [0 for _ in range(M_)]
for idx_quary in range(M_):
    ptr_s, ptr_e = map(int, sys.stdin.readline().split())
    lst_quary.append((ptr_s - 1, ptr_e - 1, idx_quary))

lst_quary.sort(key=lambda x: x[1])
lst_quary.sort(key=lambda x: x[0] // C_)

lst_count = [0 for _ in range(1000001)]
count_ = 0
ptr_curr_s = lst_quary[0][0]
ptr_curr_e = ptr_curr_s - 1

for ptr_s, ptr_e, idx_quary in lst_quary:
    while ptr_curr_s != ptr_s:
        if ptr_curr_s < ptr_s:
            val_ = lst_[ptr_curr_s]
            ptr_curr_s += 1
            if lst_count[val_] == 1:
                count_ -= 1
            lst_count[val_] -= 1
        else:
            ptr_curr_s -= 1
            val_ = lst_[ptr_curr_s]
            if lst_count[val_] == 0:
                count_ += 1
            lst_count[val_] += 1

    while ptr_curr_e != ptr_e:
        if ptr_curr_e < ptr_e:
            ptr_curr_e += 1
            val_ = lst_[ptr_curr_e]
            if lst_count[val_] == 0:
                count_ += 1
            lst_count[val_] += 1

        else:
            val_ = lst_[ptr_curr_e]
            ptr_curr_e -= 1
            if lst_count[val_] == 1:
                count_ -= 1
            lst_count[val_] -= 1

    lst_answer[idx_quary] = count_

for each_ in lst_answer:
    print(each_)
