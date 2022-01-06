import sys

DIV_ = 1000000007

lst_ = []
lst_.append(1)
lst_.append(1)
for cnt_ in range(2, 4000002):
    lst_.append((lst_[-1] * cnt_) % DIV_)


def mypow_(val_a, val_b):
    if not val_b:
        return 1
    elif val_b % 2:
        return (val_a * mypow_(val_a, val_b - 1) % DIV_) % DIV_
    else:
        return mypow_((val_a * val_a) % DIV_, val_b // 2) % DIV_


for _ in range(int(sys.stdin.readline())):
    N_, K_ = map(int, sys.stdin.readline().split())
    temp_ = lst_[K_] * lst_[N_ - K_] % DIV_
    print(lst_[N_] * mypow_(temp_, DIV_ - 2) % DIV_)

exit()
