import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

lst_ = []
val_ = 1
val_sq = 1
while val_sq <= min(10000, N):
    if val_sq >= M:
        lst_.append(val_sq)
    val_ += 1
    val_sq = val_ ** 2

if lst_:
    print(sum(lst_))
    print(lst_[0])
else:
    print(-1)

exit()