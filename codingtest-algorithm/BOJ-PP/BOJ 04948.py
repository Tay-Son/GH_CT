import sys

lst_ = []
dct_ = dict()
ptr_ = 0
input_ = int(sys.stdin.readline())
while input_:
    dct_[input_] = ptr_
    ptr_ += 1
    lst_.append((input_, -1))
    lst_.append((input_ * 2, 1))
    input_ = int(sys.stdin.readline())

N_ = max(dct_.keys()) * 2

lst_ip = [True for _ in range(N_ + 1)]

exit()
