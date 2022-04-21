import sys

N_ = int(sys.stdin.readline())
if N_ > 1:
    div_, mod_ = divmod(N_, 2)
    div_ += mod_
    print(div_)
else:
    print(0)
exit()
