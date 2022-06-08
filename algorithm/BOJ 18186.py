import sys

N_, B_, C_ = map(int, sys.stdin.readline().split())
lst_ = list(map(int, sys.stdin.readline().split()))

if B_ <= C_:
    print(sum(lst_) * B_)
else:
    cnt_b = 0
    cnt_bc = 0
    cnt_bc2 = 0

    for idx_ in range(N_ - 2):
        if lst_[idx_ + 2] < lst_[idx_ + 1]:
            val_ = min(lst_[idx_], lst_[idx_ + 1] - lst_[idx_ + 2])
            cnt_bc += val_
            lst_[idx_] -= val_
            lst_[idx_ + 1] -= val_

        val_ = min(lst_[idx_:idx_ + 3])
        cnt_bc2 += val_
        lst_[idx_] -= val_
        lst_[idx_ + 1] -= val_
        lst_[idx_ + 2] -= val_

        cnt_b += lst_[idx_]

    val_ = min(lst_[-2:])
    cnt_bc += val_
    lst_[-2] -= val_
    lst_[-1] -= val_
    cnt_b += lst_[-2] + lst_[-1]

    print(cnt_b * B_ + cnt_bc * (B_ + C_) + cnt_bc2 * (B_ + C_ + C_))

exit()
