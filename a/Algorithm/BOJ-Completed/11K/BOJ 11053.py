import sys

N = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_s = []

for idx_sub in range(0, N):
    max_ = 0
    for idx_tar in range(0, idx_sub):
        if lst_[idx_tar] < lst_[idx_sub]:
            max_ = max(max_, lst_s[idx_tar])
    lst_s.append(max_ + 1)
print(max(lst_s))
