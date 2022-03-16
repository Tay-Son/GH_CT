import sys

N_, K_ = map(int, sys.stdin.readline().split())

lst_ = []
cnt_ = 1
for each_ in map(int, sys.stdin.readline().split()):
    if each_ <= K_:
        cnt_ += 1
    else:
        lst_.append(cnt_)
        cnt_ = 1
lst_.append(cnt_)

max_ = lst_[0]
for idx_ in range(len(lst_) - 1):
    max_ = max(max_, lst_[idx_] + lst_[idx_ + 1])

print(max_)

exit()
