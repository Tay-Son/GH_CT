import sys

N_ = int(sys.stdin.readline())
dct_ = dict()
for cnt_ in range(N_):
    dct_[sys.stdin.readline().rstrip()] = cnt_
stk_ = []
tot_ = 0
for _ in range(N_):
    temp_ = dct_[sys.stdin.readline().rstrip()]
    while stk_ and stk_[-1] > temp_:
        stk_.pop()
        tot_ += 1
    stk_.append(temp_)
print(tot_)

exit()
