import sys
from collections import Counter

N_, M_ = map(int, sys.stdin.readline().split())
lst_ = [sys.stdin.readline().rstrip() for _ in range(N_)]
K_ = int(sys.stdin.readline())

max_ = 0

for r_ in range(N_):
    num_0 = Counter(lst_[r_])['0']
    cnt_ = 0
    if num_0 <= K_ and (num_0 % 2) == (K_ % 2):
        for r_sub in range(N_):
            if lst_[r_] == lst_[r_sub]:
                cnt_ += 1
    max_ = max(max_, cnt_)

print(max_)
exit()
