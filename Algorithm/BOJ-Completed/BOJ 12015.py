import sys

N = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

lst_answer = [lst_[0]]
for idx_ in range(1, len(lst_)):
    val_temp = lst_[idx_]
    if val_temp > lst_answer[-1]:
        lst_answer.append(val_temp)
    else:
        idx_l = 0
        idx_r = len(lst_answer)-1

        while idx_l < idx_r:
            idx_t = (idx_l + idx_r) // 2
            if lst_answer[idx_t] >= val_temp:
                idx_r = idx_t
            else:
                idx_l = idx_t + 1
        lst_answer[idx_r] = val_temp
print(len(lst_answer))