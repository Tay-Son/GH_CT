import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))
lst_answer = [1 for _ in range(N_)]
for idx_ in range(N_):
    for idx_sub in range(idx_):
        if lst_[idx_sub] < lst_[idx_]:
            lst_answer[idx_] += lst_answer[idx_sub]
            lst_answer[idx_] %= 998244353
print(' '.join(map(str, lst_answer)))

exit()
