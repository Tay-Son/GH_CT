import sys

A_, B_ = map(int, sys.stdin.readline().split())

INF_ = 10 ** 9
min_ = INF_


def search_(val_curr, depth_):
    global min_

    if val_curr > B_:
        pass
    elif val_curr == B_:
        min_ = min(min_, depth_)
    else:
        depth_ += 1
        search_(val_curr * 10 + 1, depth_)
        search_(val_curr * 2, depth_)


search_(A_, 1)
if min_ != INF_:
    print(min_)
else:
    print(-1)

exit()