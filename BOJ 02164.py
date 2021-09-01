import sys
from collections import deque

N_ = int(sys.stdin.readline())

deq_ = deque(range(1, N_ + 1))

while len(deq_) > 1:
    deq_.popleft()
    deq_.append(deq_.popleft())
print(deq_[0])

exit()
