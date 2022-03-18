import sys

# from bisect import bisect_left

N_ = int(sys.stdin.readline())
lst_ = []
max_ = 0
for _ in range(N_):
    value_ = int(sys.stdin.readline())
    if value_ > max_ - N_:
        max_ = max(max_, value_)
        lst_.append(value_)

lst_.sort(reverse=True)

cnt_ = 0
max_ = lst_[0] - N_
for idx_, each_ in enumerate(lst_):
    max_ = max(max_, each_ + idx_ - N_)
    if each_ > max_:
        cnt_ += 1
        print(each_, max_, max_ - N_)
    elif each_ < lst_[0] - N_:
        break

print(cnt_)

exit()
