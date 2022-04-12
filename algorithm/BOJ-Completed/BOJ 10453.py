import sys

for _ in range(int(sys.stdin.readline())):
    str_a, str_b = sys.stdin.readline().split()
    lst_ = []
    for idx_, chr_ in enumerate(str_a):
        if chr_ == 'a':
            lst_.append(idx_)
    tot_ = 0
    ptr_ = 0
    for idx_, chr_ in enumerate(str_b):
        if chr_ == 'a':
            tot_ += abs(lst_[ptr_] - idx_)
            ptr_ += 1
    print(tot_)
exit()
