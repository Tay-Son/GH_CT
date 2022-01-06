import sys

N = int(sys.stdin.readline())
lst_ = []
for _ in range(N):
    lst_.append(list(map(int, sys.stdin.readline().split())))

sum_ = (lst_[N - 1][0] + lst_[0][0]) * (lst_[N - 1][1] - lst_[0][1])
for idx_ in range(N - 1):
    sum_ += (lst_[idx_][0] + lst_[idx_ + 1][0]) * (lst_[idx_][1] - lst_[idx_ + 1][1])

print(round(abs(sum_) * 0.5, 1))