import sys
from collections import deque

grp_ = [[] for _ in range(12)]

for _ in range(12):
    a_, b_ = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    grp_[a_].append(b_)
    grp_[b_].append(a_)

for idx_ in range(12):
    min_, max_ = 12, 0
    que_ = deque([(idx_, 0)])
    lst_iv = [False for _ in range(12)]
    lst_iv[idx_] = True
    while que_:
        idx_s, depth_ = que_.popleft()
        cnt_ = 0
        for idx_t in grp_[idx_s]:
            if not lst_iv[idx_t]:
                lst_iv[idx_t] = True
                cnt_ += 1
                que_.append((idx_t, depth_ + 1))

        if not cnt_:
            min_ = min(min_, depth_)
            max_ = max(max_, depth_)

    print(idx_, min_, max_)
    if min_ == 1 and max_ == 5:
        print(idx_ + 1)
        break

exit()
