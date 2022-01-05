import sys
from collections import deque

INF_ = 1000007

F_, S_, G_, U_, D_ = map(int, sys.stdin.readline().split())

que_ = deque()

lst_iv = [INF_ for _ in range(F_ + 1)]
que_.append((S_, 0))

while que_:
    curr_, depth_ = que_.popleft()
    if depth_ < lst_iv[curr_]:
        lst_iv[curr_] = depth_

        if curr_ == G_:
            break

        depth_ += 1
        for offset_ in [U_, -D_]:
            target_ = curr_ + offset_
            if 0 < target_ <= F_ and lst_iv[target_] > depth_:
                que_.append((target_, depth_))

print(lst_iv[G_] if lst_iv[G_] != INF_ else 'use the stairs')
print(lst_iv)

exit()
