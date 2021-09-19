import sys
lst_ = list(map(int, sys.stdin.readline().split()))
while sum(lst_) != 0:
    lst_.sort()
    if lst_[0]**2 + lst_[1]**2 == lst_[2]**2:
        print('right')
    else:
        print('wrong')
    lst_ = list(map(int, sys.stdin.readline().split()))