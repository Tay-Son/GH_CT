import sys
from collections import Counter

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
dct_ = Counter(lst_).items()
if 0 not in dct_:
    dct_[0] = 0

max_ = -1
for key_, val_ in dct_.items():
    if key_ == val_:
        max_ = max(max_, key_)
print(max_)

exit()
