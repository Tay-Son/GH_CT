import sys

str_ = sys.stdin.readline().rstrip()
set_ = set()
for idx_s in range(len(str_)):
    for idx_e in range(idx_s+1, len(str_) + 1):
        set_.add(str_[idx_s:idx_e])
print(len(set_))

exit()