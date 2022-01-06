import sys
from collections import deque

N_, M_ = map(int, sys.stdin.readline().split())
lst_ = [0 for _ in range(101)]

for _ in range(N_ + M_):
    idx_s, idx_e = map(int, sys.stdin.readline().split())
    lst_[idx_s] = idx_e

que_ = deque()
que_.append((1, 0))

lst_iv = [101 for _ in range(101)]

while que_:
    idx_s, depth_ = que_.popleft()
    if lst_iv[idx_s] > depth_:
        lst_iv[idx_s] = depth_
        temp_ = lst_[idx_s]
        if temp_:
            que_.append((temp_, depth_))
        else:
            depth_ += 1
            for offset_ in range(1, 7):
                idx_t = idx_s + offset_
                if idx_t <= 100:
                    que_.append((idx_t, depth_))

print(lst_iv[100])
exit()
