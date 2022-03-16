import sys

X_ = int(sys.stdin.readline())
lst_ = [0, 0, 1, 1]
if X_ > 3:
    for idx_ in range(4, X_ + 1):
        lst_temp = []
        if not idx_ % 3:
            lst_temp.append(lst_[idx_ // 3])
        if not idx_ % 2:
            lst_temp.append(lst_[idx_ // 2])
        lst_temp.append(lst_[idx_ - 1])
        lst_.append(min(lst_temp) + 1)

print(lst_[X_])

idx_ = X_
for cnt_ in range(lst_[X_], -1, -1):
    print(idx_, end=' ')
    if not idx_ % 3 and lst_[idx_ // 3] == cnt_ - 1:
        idx_ //= 3
    elif not idx_ % 2 and lst_[idx_ // 2] == cnt_ - 1:
        idx_ //= 2
    else:
        idx_ -= 1

exit()