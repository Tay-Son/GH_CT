import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(lambda x: x[0], sys.stdin.readline().split()))
for each_ in lst_[1:]:
    if each_ != lst_[0]:
        print(0)
        break
else:
    print(1)

exit()
