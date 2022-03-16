import sys
from collections import deque

N_, K_ = map(int, sys.stdin.readline().split())
deq_ = deque(range(1, N_ + 1))
cnt_ = 1
lst_ = []
while len(deq_):
    temp_ = deq_.popleft()
    if cnt_ % K_:
        deq_.append(temp_)
    else:
        lst_.append(temp_)
    cnt_ += 1
print('<' + ', '.join(map(str, lst_)) + '>')

exit()