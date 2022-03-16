import sys

K_ = int(sys.stdin.readline())

dct_ = {
    1: lambda pos_, val: (pos_[0] + val_, pos_[1]),
    2: lambda pos_, val: (pos_[0] - val_, pos_[1]),
    3: lambda pos_, val: (pos_[0], pos_[1] + val_),
    4: lambda pos_, val: (pos_[0], pos_[1] - val_)
}

lst_ = [(0, 0)]
for _ in range(5):
    d_, val_ = map(int, sys.stdin.readline().split())
    lst_.append(dct_[d_](lst_[-1], val_))
trs_, trs_ = map(int, sys.stdin.readline().split())

sum_ = 0
for idx_ in range(5):
    val_ = lst_[idx_ + 1][0] * lst_[idx_][1] - lst_[idx_][0] * lst_[idx_ + 1][1]
    sum_ += val_
val_ = lst_[0][0] * lst_[5][1] - lst_[5][0] * lst_[0][1]
sum_ += val_

print(sum_ // 2 * K_)
exit()
