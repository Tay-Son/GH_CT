import sys

N_ = int(sys.stdin.readline())
print(N_ + max(N_ - 2, 0))
for a_, b_ in [(idx_, 1) for idx_ in range(1, N_ + 1)]:
    print(a_, b_)
for a_, b_ in [(idx_, N_) for idx_ in range(2, N_)]:
    print(a_, b_)
exit()
