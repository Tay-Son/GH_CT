import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
cnt_ = 3

is_ = True
lst_mod = []
for idx_ in range(1, N_):
    if lst_[idx_] < lst_[idx_ - 1]:
        if cnt_:
            lst_[idx_] = lst_[idx_ - 1]
            lst_mod.append((idx_ + 1, lst_[idx_ - 1]))
            cnt_ -= 1
        else:
            is_ = False
            break

if is_:
    print('YES')
    print(len(lst_mod))
    for each_ in lst_mod:
        print(' '.join(map(str, each_)))
else:
    print('NO')

exit()
