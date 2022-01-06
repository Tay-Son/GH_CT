import sys
from collections import deque

N_, K_ = map(int, sys.stdin.readline().split())
MAX_SIZE = 100001

que_ = deque()
que_.append(N_)
lst_ = [-1 for _ in range(100001)]
lst_[N_] = 0

cnt_ = 0
while que_:
    c_ = que_.popleft()
    if c_ == K_:
        cnt_ += 1
    for t_ in [c_ * 2, c_ + 1, c_ - 1]:
        if 0 <= t_ <= 100000:
            if lst_[t_] == -1 or lst_[t_] >= lst_[c_] + 1:
                lst_[t_] = lst_[c_] + 1
                que_.append(t_)

print(lst_[K_])
print(cnt_)

exit()


