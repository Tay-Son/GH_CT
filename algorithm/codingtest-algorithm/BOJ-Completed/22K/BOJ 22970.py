import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

max_ = 1
ptr_ = 0
while ptr_ < N_:
    cnt_ = 1
    while ptr_ + 1 < N_ and lst_[ptr_] < lst_[ptr_ + 1]:
        ptr_ += 1
        cnt_ += 1
    while ptr_ + 1 < N_ and lst_[ptr_] > lst_[ptr_ + 1]:
        ptr_ += 1
        cnt_ += 1
    max_ = max(max_, cnt_)
    if ptr_ == N_ - 1:
        break
    elif lst_[ptr_] == lst_[ptr_ + 1]:
        ptr_ += 1
print(max_)

exit()
