import sys

lst_ = [0, 1]
temp_ = lst_[-1] + lst_[-2] + 1
while temp_ < 1000000000:
    lst_.append(temp_)
    temp_ = lst_[-1] + lst_[-2] + 1

for _ in range(int(sys.stdin.readline())):
    V_ = int(sys.stdin.readline())
    ptr_ = 1
    while ptr_ + 1 < len(lst_) and V_ >= lst_[ptr_ + 1]:
        ptr_ += 1
    print(ptr_)
exit()
