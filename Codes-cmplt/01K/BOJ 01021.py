import sys
from collections import deque

N_, M_ = map(int, sys.stdin.readline().split())
deq_ = deque(range(N_))
cnt_ = 0
for target_ in map(lambda x: int(x) - 1, sys.stdin.readline().split()):
    idx_target = deq_.index(target_)
    idx_target_r = len(deq_) - idx_target
    cnt_ += min(idx_target, idx_target_r)
    if idx_target <= idx_target_r:
        for _ in range(idx_target):
            deq_.append(deq_.popleft())
    else:
        for _ in range(idx_target_r):
            deq_.appendleft(deq_.pop())
    deq_.popleft()
print(cnt_)
exit()