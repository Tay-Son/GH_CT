import sys

N_ = int(sys.stdin.readline())
lst_a = list(map(int, sys.stdin.readline().split()))
lst_b = list(map(int, sys.stdin.readline().split()))

lst_ = [0 for _ in range(N_ + 1)]
cnt_ = 0
for each_ in lst_a:
    lst_[each_] = cnt_
    cnt_ += 1
lst_c = []
for each_ in lst_b:
    lst_c.append(lst_[each_])

lst_answer = [lst_c[0]]
for idx_ in range(1, N_):
    val_temp = lst_c[idx_]
    if val_temp > lst_answer[-1]:
        lst_answer.append(val_temp)
    else:
        idx_l = 0
        idx_r = len(lst_answer) - 1

        while idx_l < idx_r:
            idx_t = (idx_l + idx_r) // 2
            if lst_answer[idx_t] >= val_temp:
                idx_r = idx_t
            else:
                idx_l = idx_t + 1
        lst_answer[idx_r] = val_temp
print(len(lst_answer))

exit()
