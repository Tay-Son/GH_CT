import sys

N_, M_ = map(int, sys.stdin.readline().split())
lst_ = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
mat_ = []
for _ in range(N_):
    mat_.append(list(map(int, sys.stdin.readline().split())))

tot_ = 0
for idx_ in range(M_ - 1):
    s_, e_ = lst_[idx_], lst_[idx_ + 1]
    tot_ += mat_[s_][e_]

print(tot_)

exit()
