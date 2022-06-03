import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
cnt_7 = 0
cnt_5 = 0
cnt_3 = 0
for idx_ in range(N_ - 2):
    if lst_[idx_ + 2] < lst_[idx_ + 1]:
        val_ = min(lst_[idx_], lst_[idx_ + 1] - lst_[idx_ + 2])
        cnt_5 += val_
        lst_[idx_] -= val_
        lst_[idx_ + 1] -= val_

    val_ = min(lst_[idx_:idx_ + 3])
    cnt_7 += val_
    lst_[idx_] -= val_
    lst_[idx_ + 1] -= val_
    lst_[idx_ + 2] -= val_

    cnt_3 += lst_[idx_]

val_ = min(lst_[-2:])
cnt_5 += val_
lst_[-2] -= val_
lst_[-1] -= val_
cnt_3 += lst_[-2] + lst_[-1]

print(7 * cnt_7 + 5 * cnt_5 + cnt_3 * 3)

exit()
