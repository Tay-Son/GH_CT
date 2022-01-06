import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

temp_ = lst_[0]
max_ = temp_
for each_ in lst_[1:]:
    temp_ = max(0, temp_) + each_
    max_ = max(max_, temp_)
print(max_)

exit()