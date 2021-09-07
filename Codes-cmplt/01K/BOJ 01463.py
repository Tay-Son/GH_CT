import sys
from collections import deque

N_, D_ = (int(sys.stdin.readline()), 0)
deq_ = deque()

while N_ != 1:
    if not N_ % 3:
        deq_.append((N_ // 3, D_ + 1))
    if not N_ % 2:
        deq_.append((N_ // 2, D_ + 1))
    deq_.append((N_ - 1, D_ + 1))
    N_, D_ = deq_.popleft()
print(D_)

exit()