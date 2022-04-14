import sys

N_, M_ = map(int, sys.stdin.readline().split())
for _ in range(M_):
    k_ = int(sys.stdin.readline())
    lst_ = list(map(int, sys.stdin.readline().split()))
    is_failed = False
    if len(lst_) > 1:
        for a_, b_ in zip(lst_[:-1], lst_[1:]):
            if a_ < b_:
                is_failed = True
                break
    if is_failed:
        print('No')
        break
else:
    print('Yes')
exit()
