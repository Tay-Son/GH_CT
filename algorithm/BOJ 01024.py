import sys

N_, L_ = map(int, sys.stdin.readline().split())
for cand_ in range(L_, 101):
    temp_ = N_ - (cand_ * (cand_ - 1)) // 2
    if temp_ < 0:
        print(-1)
        break
    else:
        div_, mod_ = divmod(temp_, cand_)
        if not mod_:
            print(' '.join(map(str, range(div_, div_ + cand_))))
            break
else:
    print(-1)
exit()
