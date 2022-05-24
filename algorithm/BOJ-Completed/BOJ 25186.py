import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
sum_ = sum(lst_)
max_ = max(lst_)

if sum_ == 1:
    print('Happy')
else:
    print('Happy' if max_ <= sum_ // 2 else 'Unhappy')

exit()
