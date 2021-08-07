import sys

INF_ = 10 ** 9
N_ = int(sys.stdin.readline())
lst_ = []

for _ in range(N_):
    val_a, val_b, val_c = map(int, sys.stdin.readline().split())
    if val_b == 0:
        lst_.append((INF_, val_c / val_a))
    elif val_a == 0:
        lst_.append((0, val_c / val_b))
    else:
        lst_.append((val_a / val_b, val_c / val_b))

lst_.sort()

ans_ = (N_ * (N_ - 1)) // 2
cnt_ = 0

for idx_ in range(N_ - 1):
    if lst_[idx_][0] == lst_[idx_ + 1][0]:
        if lst_[idx_][1] != lst_[idx_ + 1][1]:
            cnt_ += 1
            ans_ -= cnt_
        else:
            cnt_ = 0
    else:
        cnt_ = 0

print(ans_)

exit()
