import sys

N_ = int(sys.stdin.readline())
lst_ = [0] + list(map(int, sys.stdin.readline().split()))
lst_answer = [0 for _ in range(N_ + 1)]
stk_ = []
for idx_ in range(N_, 0, -1):
    while len(stk_) and stk_[-1][0] <= lst_[idx_]:
        lst_answer[stk_[-1][1]] = idx_
        stk_.pop()
    stk_.append((lst_[idx_], idx_))

print(' '.join(map(str, lst_answer[1:])))

exit()